from django.contrib import admin
from gamestore.models import Game, Score, Purchase, Save

admin.site.register(Game)
admin.site.register(Score)
admin.site.register(Purchase)
admin.site.register(Save)
