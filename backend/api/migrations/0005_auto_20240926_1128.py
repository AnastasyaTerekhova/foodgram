# Generated by Django 3.2.3 on 2024-09-26 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20240925_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientsrecipe',
            options={'ordering': ('recipe',), 'verbose_name': 'Количество ингредиента', 'verbose_name_plural': 'Количество ингредиентов'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('-created_at',), 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredientsrecipe',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AddConstraint(
            model_name='ingredientsrecipe',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredients'), name='уникальное значение'),
        ),
    ]