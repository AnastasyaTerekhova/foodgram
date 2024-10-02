from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_LENGTH_EMAIL = 254
MAX_LENGTH_TEXT = 150


class Tags(models.Model):
    """Модель для тегов."""

    name = models.CharField('Название тега', max_length=30)
    slug = models.SlugField('Слаг для тегов', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    """Модель для ингредиентов."""

    name = models.CharField('Название ингредиента', max_length=30)
    measurement_unit = models.CharField('Единицы измерения', blank=False,
                                        max_length=50)
    amount = models.CharField(
        'Колличество',
        max_length=50,
        blank=True
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель для рецептов."""

    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               on_delete=models.CASCADE)
    name = models.CharField('Название рецепта', blank=False,
                            max_length=MAX_LENGTH_TEXT)
    image = models.ImageField('Картинка', blank=True,
                              default=None, upload_to='recipes/images/')
    text = models.CharField('Описание рецепта', max_length=MAX_LENGTH_TEXT)
    ingredients = models.ManyToManyField(Ingredients)
    tags = models.ManyToManyField(Tags, through='TagsRecipe')
    cooking_time = models.CharField('Время приготовления', max_length=30)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата публикации')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class TagsRecipe(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tags} {self.recipe}'


class IngredientsRecipe(models.Model):
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField('Количество', default=1)

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredients'],
                name='уникальное значение')]

    def __str__(self):
        return f'{self.ingredients} {self.recipe}'


class UserRecipeModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        abstract = True


class Favorite(UserRecipeModel):

    class Meta(UserRecipeModel.Meta):
        default_related_name = 'favorites'
        verbose_name = 'Избранное'

    def __str__(self):
        return (
            f'Пользователь {self.user.username} добавил в избранное '
            f' рецепт {self.recipe}'
        )


class ShoppingCart(UserRecipeModel):

    class Meta(UserRecipeModel.Meta):
        default_related_name = 'shopping_cart'
        verbose_name = 'Избранное'

    def __str__(self):
        return (
            f'Пользователь {self.user.username} добавил в список '
            f' покупок рецепт {self.recipe}'
        )