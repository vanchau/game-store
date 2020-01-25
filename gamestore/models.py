from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# All users are players, but players can also be developers
class User(AbstractUser):
    pass
    # username provided as default attribute in django

class Developer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

class Game(models.Model):
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(editable=True)
    on_sale = models.BooleanField()
    url = models.URLField()
    scores = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #game_id = ... # given automatically for each model as a primary key "id"
    purchased_time = models.DateTimeField(auto_now_add=True)
    price_paid = models.PositiveSmallIntegerField(editable=False)

class SavedGame(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    play_data = models.CharField(max_length=100)
    
    def create(self, title):
        saved_data = self.player_data=title
        # do something with the book
        return saved_data