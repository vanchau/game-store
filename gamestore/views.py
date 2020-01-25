from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

def index(request):
   return render(request, "gamestore/home.html", {})

class GameListView(ListView):
    model = models.Game