from django.contrib import admin
from gamestore.models import User, Game, Score, Purchase

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Score)
admin.site.register(Purchase)
