from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField()
    allergens = models.CharField(max_length=55)
    preparation_time = models.IntegerField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
