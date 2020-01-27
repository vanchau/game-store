from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

class HomeView(ListView):
   model = models.Game
   template_name = 'gamestore/home.html'

class GameView(DetailView):
   model = models.Game
   template_name = 'gamestore/game.html'
