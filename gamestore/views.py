from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                 CreateView, DeleteView, UpdateView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from gamestore.models import (Game, Purchase)
from hashlib import md5
from braces.views import SelectRelatedMixin
import uuid

from django.contrib.auth import get_user_model
User = get_user_model()

# Home view. Display all available games.
class HomeView(ListView):
   model = Game
   template_name = 'gamestore/home.html'

# Game view. Users can (depending on their role) modify, delete, play, or purchase games.
class GameView(DetailView):
   model = Game
   template_name = 'gamestore/game_view.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Check if a completed purchase instance exists for this particular game and the user. 
      if (self.request.user.is_authenticated and
         Purchase.objects.filter(
            game__id=self.kwargs['pk'],
            player=self.request.user,
            purchase_complete=True
         ).exists()):
         context["purchased_game"] = True
      else:
         context["purchased_game"] = False
      return context

# Inventory view. Developers can quickly access their games here.
class UserInventory(LoginRequiredMixin, ListView):
   model = Game
   template_name = "gamestore/inventory.html"

   def get_queryset(self):
      purchases = self.model.objects.filter(publisher_id=self.request.user.id)
      queryset = purchases
      return queryset

# Statistics view. Displays sale data such as paid price, purchased date, etc.
class StatisticsView(LoginRequiredMixin, SelectRelatedMixin, ListView):
   model = Purchase
   template_name = "gamestore/statistics.html"

   def get_queryset(self, **kwargs):
      purchases = self.model.objects.filter(game__id=self.kwargs['pk'], purchase_complete=True)
      queryset = purchases
      return queryset
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      purchases = self.model.objects.filter(game__id=self.kwargs['pk'], purchase_complete=True)
      # Provide the total number of completed transactions (i.e. purchased games).
      context["purchase_total_count"] = purchases.count()
      sum = 0
      if purchases.count() > 0:
         for purchase in purchases:
            sum = sum + purchase.paid_price
      # Total revenue of the game.
      context["revenue"] = sum
      context["game_title"] = Game.objects.get(id=self.kwargs['pk']).title
      return context

# View for displaying purchased games.
class PurchasedGames(LoginRequiredMixin, ListView):
   model = Purchase
   template_name = 'gamestore/my_games.html'

   def get_queryset(self):
      queryset = self.model.objects.filter(player=self.request.user).select_related('game')
      return queryset

# View for uploading a new game instance. Uses the template game_form.html.
class PublishGame(LoginRequiredMixin, CreateView):
   # Fields to be displayed in the view.
   fields = ('title', 'price', 'description', 'url')
   model = Game

   # Called when valid form data has been POSTed.
   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.publisher = self.request.user
      self.object.save()
      return super().form_valid(form)

# View for deleting a game. Loads game_confirm_delete.html template.
class DeleteGame(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
   model = Game
   success_url = reverse_lazy("games:home")
   select_related = ("publisher",)

   def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(publisher_id=self.request.user.id)

   def delete(self, *args, **kwargs):
      messages.success(self.request, "Game Deleted")
      return super().delete(*args, **kwargs)

# Used for modifying an existing game.
class UpdateGame(LoginRequiredMixin, UpdateView):
   model = Game
   fields = ['title', 'price', 'description', 'url']
   template_name = 'gamestore/game_update_form.html'

# View presented prior to redirecting the user to payment service.
class PurchaseGame(LoginRequiredMixin, TemplateView):
   template_name = 'gamestore/purchase_form.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      game = Game.objects.get(id=self.kwargs['game_id'])
      payment_id = uuid.uuid1() # generate a unique identifier for pid

      # Generate the checksum string before applying md5 hashing.
      checksumstr = "pid={pid}&sid={sid}&amount={amount}&token={secret}".format(
         pid=payment_id,
         sid='lwUGtWdhbWVzY29wZQ==',
         amount=game.price,
         secret='DleOGf86zXN40AajmCR4Q8vZVYkA'
      )

      checksum = md5(checksumstr.encode('utf-8')).hexdigest()
      # Find if there is an incomplete (non-finalized) purchase instance.
      failed_purchase = Purchase.objects.filter(player=self.request.user, game=game, purchase_complete=False)

      if failed_purchase.exists():
         failed_purchase.delete()

      # Create a new purchase instance.
      new_purchase = Purchase(pid=payment_id, player=self.request.user, game=game, paid_price=game.price)
      new_purchase.save()

      context["checksum"] = checksum
      context["pid"] = payment_id
      context['game'] = game
      return context

# Success view to which a user will be redirected to after a successful purchase.
class SuccessView(LoginRequiredMixin, TemplateView):
   template_name = 'purchase/error.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      pid = self.request.GET.get('pid')
      status = self.request.GET.get('result')
      purchase_data = Purchase.objects.get(pid=pid)

      if status == 'success':
         purchase_data.purchase_complete=True
         purchase_data.save()
         self.template_name = 'purchase/success.html'
      else:
         purchase_data.delete()
      return context

# Cancel view for cancelled purchases.
class CancelView(LoginRequiredMixin, TemplateView):
   template_name = 'purchase/cancel.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      pid = self.request.GET.get('pid')
      purchase_data = Purchase.objects.get(pid=pid)
      purchase_data.delete()
      return context

# Error view for failed purchase attempts.
class ErrorView(LoginRequiredMixin, TemplateView):
   template_name = 'purchase/error.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      pid = self.request.GET.get('pid')
      purchase_data = Purchase.objects.get(pid=pid)
      purchase_data.delete()
      return context
   