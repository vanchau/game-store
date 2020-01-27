from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Game(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField(editable=True)
    description = models.CharField(max_length=200)
    publisher = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField()

    def get_absolute_url(self):
        return reverse(
            "games:game",
            kwargs={
                "pk": self.pk
            }
        )

class Purchase(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchased_time = models.DateTimeField(auto_now_add=True)

class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    play_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(editable=False)