from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Player & Developer
# Username provided as default attribute in django
class User(AbstractUser):
    pass

class Game(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField(editable=True)
    info_text = models.CharField(max_length=30)
    developerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
    playerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gameID = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchased_time = models.DateTimeField(auto_now_add=True)

class Score(models.Model):
    playerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gameID = models.ForeignKey(Game, on_delete=models.CASCADE)
    play_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(editable=False)