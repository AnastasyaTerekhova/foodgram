# Generated by Django 3.2.3 on 2024-09-26 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_ingredients_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='amount',
            field=models.CharField(blank=True, max_length=50, verbose_name='Колличество'),
        ),
        migrations.AlterField(
            model_name='ingredientsrecipe',
            name='amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Колличество ингредиента не может быть меньше 1')], verbose_name='Количество'),
        ),
    ]
