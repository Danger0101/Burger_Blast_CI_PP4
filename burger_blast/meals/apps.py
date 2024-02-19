'''
This file is used to configure the app name for the meals app
'''
from django.apps import AppConfig


class MealsConfig(AppConfig):
    '''
    Configuration for the meals app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meals'
