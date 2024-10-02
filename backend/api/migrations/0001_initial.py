# Generated by Django 3.2.3 on 2024-09-19 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название ингредиента')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='Единицы измерения')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('name', models.CharField(max_length=150, verbose_name='Название рецепта')),
                ('image', models.ImageField(blank=True, default=None, upload_to='recipes/images/', verbose_name='Картинка')),
                ('text', models.CharField(max_length=150, verbose_name='Описание рецепта')),
                ('cooking_time', models.CharField(max_length=30, verbose_name='Время приготовления')),
                ('ingredients', models.ManyToManyField(to='api.Ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название тега')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг для тегов')),
            ],
        ),
        migrations.CreateModel(
            name='TagsRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recipe')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tags')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(through='api.TagsRecipe', to='api.Tags'),
        ),
        migrations.CreateModel(
            name='IngredientsRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ingredients')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recipe')),
            ],
        ),
    ]
