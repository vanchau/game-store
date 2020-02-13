from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.GameView.as_view(), name='game'),
    path('my-inventory', views.UserInventory.as_view(), name='inventory'),
    path('new', views.PublishGame.as_view(), name='publish'),
    path('my-games', views.PurchasedGames.as_view(), name='purchased'),
    path('delete/<int:pk>', views.DeleteGame.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateGame.as_view(), name='update'),
    path('purchase/<int:game_id>', views.PurchaseGame.as_view(), name='purchase'),
    path('purchase/success', views.SuccessView.as_view(), name='success'),
    path('purchase/cancel', views.CancelView.as_view(), name='cancel'),
    path('purchase/error', views.ErrorView.as_view(), name='error'),
    path('statistics/<int:pk>', views.StatisticsView.as_view(), name='statistics'),
    url(r'^ajax/score/$', views.score, name='score')
]
