# Generated by Django 3.2.3 on 2024-09-30 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_subscribed',
        ),
    ]