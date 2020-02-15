from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

User = get_user_model()

# Contain information relevant to a game: game title, price, description,
# creator (publisher), game url, category, etc.
class Game(models.Model):
    CATEGORY_CHOICES = (
        ('Adventure','Adventure',),
        ('Action','Action',),
        ('Puzzle','Puzzle',),
        ('Strategy','Strategy',),
        ('Other', 'Other',)
    )
    title = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField(editable=True)
    description = models.CharField(max_length=200)
    publisher = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def get_absolute_url(self):
        return reverse("games:game", kwargs={ "pk": self.pk })

# Store purchase information whenever a game is bought or is about to be bought.
# player info, purchased game, purchase status (True/False), paid price (used for statistics), etc. 
class Purchase(models.Model):
    pid = models.UUIDField(primary_key=True, editable=False)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchased_time = models.DateTimeField(auto_now_add=True)
    purchase_complete = models.BooleanField(default=False)
    paid_price = models.PositiveSmallIntegerField(editable=False)
    # checksum = models.CharField(max_length=32, editable=False)

# Store game scores produced by players.
class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    play_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(editable=False)

# Store game data.
class Save(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    save_date = models.DateTimeField(auto_now_add=True)
    game_state = models.TextField()
  