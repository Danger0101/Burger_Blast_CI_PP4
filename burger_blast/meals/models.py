from django.db import models

class Meal(models.Model):
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

    def __str__(self):
        return self.name
