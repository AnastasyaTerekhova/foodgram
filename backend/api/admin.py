from django.contrib import admin

from .models import Favorite, Ingredients, Recipe, ShoppingCart, Tags


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    list_display_links = ('id', 'author')
    search_fields = ('name', 'author')


admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
