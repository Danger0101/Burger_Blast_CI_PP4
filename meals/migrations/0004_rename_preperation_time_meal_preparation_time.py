# Generated by Django 5.0.1 on 2024-01-15 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_alter_meal_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='preperation_time',
            new_name='preparation_time',
        ),
    ]
