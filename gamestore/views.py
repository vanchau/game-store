from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                 CreateView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from . import models
# pip install django-braces
from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

class HomeView(ListView):
   model = models.Game
   template_name = 'gamestore/home.html'

class GameView(DetailView):
   model = models.Game
   template_name = 'gamestore/game_view.html'

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