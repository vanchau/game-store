from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.GameView.as_view(), name='game'),
    path('<username>/', views.UserInventory.as_view(), name='inventory'),
    path('new/', views.PublishGame.as_view(), name='publish'),
    path('delete/<int:pk>/', views.DeleteGame.as_view(), name='delete'),
]
