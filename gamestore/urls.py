from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game-list/', views.GameListView.as_view(), name='list'),
]
