# Generated by Django 5.0.2 on 2024-02-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_remove_meal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.CharField(choices=[('Entree', 'Entree'), ('Side Dishes', 'Side Dishes'), ('Desserts', 'Desserts')], default='Entree', max_length=20),
        ),
    ]
