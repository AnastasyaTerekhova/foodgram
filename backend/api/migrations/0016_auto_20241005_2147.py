# Generated by Django 3.2.3 on 2024-10-05 18:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0015_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'default_related_name': 'recipes', 'ordering': ['name', 'author'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1, 'Время приготовления не может быть меньше 1 минуты.'), django.core.validators.MaxLengthValidator(1440, 'Cлишком большое значение')], verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='api.IngredientsRecipe', to='api.Ingredients', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', through='api.TagsRecipe', to='api.Tags', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=models.TextField(max_length=100000, verbose_name='Описание рецепта'),
        ),
        migrations.AddConstraint(
            model_name='ingredients',
            constraint=models.UniqueConstraint(fields=('name', 'measurement_unit'), name='unique ingredient name and measurement unit'),
        ),
    ]
