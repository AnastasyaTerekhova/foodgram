# Generated by Django 3.2.3 on 2024-09-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_ingredients_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientsrecipe',
            name='amount',
            field=models.CharField(blank=True, max_length=50, verbose_name='Количество'),
        ),
    ]
