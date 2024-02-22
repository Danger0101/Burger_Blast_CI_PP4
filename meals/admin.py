'''
This file is used to register the Meal model with the Django admin
so that we can manage the meals from the admin interface.
'''
from django.contrib import admin
from .models import Meal

admin.site.register(Meal)
