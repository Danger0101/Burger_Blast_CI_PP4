from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=500)
    # Add a field for the number of people the meal serves
    people = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='meals/', null=True, blank=True)
    calories = models.IntegerField()
    allergens = models.CharField(max_length=55)
    preperation_time = models.IntegerField()

    def __str__(self):
        return self.name
