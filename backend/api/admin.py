from django.contrib import admin
from users.admin import BaseAdmin

from .models import (Favorite, Ingredients, IngredientsRecipe, Recipe,
                     ShoppingCart, Tags)


class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientsRecipe
    extra = 0
    min_num = 1


@admin.register(Ingredients)
class IngredientAdmin(BaseAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    inlines = (IngredientInRecipeInline, )


@admin.register(Tags)
class TagAdmin(BaseAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    list_filter = ('name', )


@admin.register(Recipe)
class RecipeAdmin(BaseAdmin):
    list_display = (
        'name',
        'author',
        'text',
        'cooking_time',
        'created_at',
        'favorites_count',
        'display_ingredients'
    )
    search_fields = ('name', 'author__username', 'favorites_count')
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientInRecipeInline,)

    @admin.display(description="Число добавлений в избранное")
    def favorites_count(self, obj):
        return obj.favorites.count()

    @admin.display(description="Отображение ингредиентов")
    def display_ingredients(self, recipe):
        return ', '.join([
            ingredients.name for ingredients in recipe.ingredients.all()])


@admin.register(ShoppingCart)
class ShoppingCartAdmin(BaseAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user',)


@admin.register(Favorite)
class FavoriteAdmin(BaseAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user',)
