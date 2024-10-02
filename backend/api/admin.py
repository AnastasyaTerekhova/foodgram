from django.contrib import admin

from .models import Favorite, Ingredients, Recipe, Tags

admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Recipe)
admin.site.register(Favorite)