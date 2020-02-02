from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                 CreateView, DeleteView, UpdateView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from . import models
from hashlib import md5
# pip install django-braces
from braces.views import SelectRelatedMixin
import uuid

from django.contrib.auth import get_user_model
User = get_user_model()

class HomeView(ListView):
   model = models.Game
   template_name = 'gamestore/home.html'

class GameView(DetailView):
   model = models.Game
   template_name = 'gamestore/game_view.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      purchase_model = models.Purchase

      if models.Purchase.objects.filter(game__id=self.kwargs['pk'], player=self.request.user):
         context["owned_game"] = True
      else:
         context["owned_game"] = False
      return context

class UserInventory(ListView):
   model = models.Game
   template_name = "gamestore/inventory.html"

   def get_queryset(self):
      try:
         self.game_publisher = User.objects.prefetch_related("games",).get(
            username__iexact=self.request.user.username
         )
      except User.DoesNotExist:
         raise Http404
      else:
         return self.game_publisher.games.all().filter(publisher_id=self.request.user.id)

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # add publisher into the context so that it can be used in the template
      context["game_publisher"] = self.game_publisher 
      return context

class PurchasedGames(ListView):
   model = models.Purchase
   template_name = 'gamestore/my_games.html'

   def get_queryset(self):
      queryset = self.model.objects.filter(player=self.request.user).select_related('game')
      return queryset

class PublishGame(LoginRequiredMixin, CreateView):
   fields = ('title', 'price', 'description', 'url')
   model = models.Game

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.publisher = self.request.user
      self.object.save()
      return super().form_valid(form)

class DeleteGame(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
   model = models.Game
   success_url = reverse_lazy("games:home")
   select_related = ("publisher",)

   def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(publisher_id=self.request.user.id)

   def delete(self, *args, **kwargs):
      messages.success(self.request, "Game Deleted")
      return super().delete(*args, **kwargs)

class PurchaseGame(LoginRequiredMixin, TemplateView):
   template_name = 'gamestore/purchase_form.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      game = models.Game.objects.get(id=self.kwargs['game_id'])
      payment_id = uuid.uuid1()

      checksumstr = "pid={pid}&sid={sid}&amount={amount}&token={secret}".format(
         pid=payment_id,
         sid='lwUGtWdhbWVzY29wZQ==',
         amount=game.price,
         secret='DleOGf86zXN40AajmCR4Q8vZVYkA'
      )

      checksum = md5(checksumstr.encode('utf-8')).hexdigest()
      new_purchase = models.Purchase(pid=payment_id, player=self.request.user, game=game)
      new_purchase.save()

      context["checksum"] = checksum
      context["pid"] = payment_id
      context['game'] = game
      return context

class SuccessView(TemplateView):
   template_name = 'purchase/error.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      pid = self.request.GET.get('pid')
      status = self.request.GET.get('result')
      purchase_data = models.Purchase.objects.get(pid=pid)

      if status == 'success':
         print('TRUE')
         self.template_name = 'purchase/success.html'
      else:
         print('FALSE')
         purchase_data.delete()
      return context

class CancelView(TemplateView):
   template_name = 'purchase/cancel.html'

class ErrorView(TemplateView):
   template_name = 'purchase/error.html'
   