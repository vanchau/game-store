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

class HomeView(ListView):
   model = models.Game
   template_name = 'gamestore/home.html'

class GameView(DetailView):
   model = models.Game
   template_name = 'gamestore/game.html'

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