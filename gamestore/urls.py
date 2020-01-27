from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.GameView.as_view(), name='game'),
    path('delete/<int:pk>/', views.DeleteGame.as_view(), name="delete"),
]
