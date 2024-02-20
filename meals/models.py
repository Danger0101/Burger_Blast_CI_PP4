'''
This module contains the model for a meal.
'''
from django.db import models


class Meal(models.Model):
    '''
    Model for a meal.

    Attributes:
        name (str): The name of the meal.
        description (str): A description of the meal.
        people (int): The number of people the meal serves.
        price (float): The price of the meal.
        calories (int): The number of calories in the meal.
        allergens (str): A list of allergens in the meal.
        preparation_time (int): The time it takes to prepare the meal.
        slug (str): The slug for the meal.
        category (str): The category of the meal.
    '''
    ENTREE = 'Entree'
    SIDE_DISH = 'Side Dishes'
    DESSERT = 'Desserts'

    CATEGORY_CHOICES = [
        (ENTREE, 'Entree'),
        (SIDE_DISH, 'Side Dishes'),
        (DESSERT, 'Desserts'),
    ]

    DEFAULT_CATEGORY = ENTREE

    name = models.CharField(max_length=55)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField()
    allergens = models.CharField(max_length=55)
    preparation_time = models.IntegerField()
    slug = models.SlugField(blank=True, null=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=DEFAULT_CATEGORY
    )
