'''
Contains the url patterns for the meals app.
'''
from django.urls import path
from .views import menu_view, create_or_update_meal, meal_detail

app_name = 'meals'

urlpatterns = [
    path('menu/', menu_view, name='menu'),
    path('create-meal/', create_or_update_meal, name='create_meal'),
    path(
        'update-meal/<int:meal_id>/',
        create_or_update_meal,
        name='update_meal'
    ),
    path('meal-detail/<slug:slug>/', meal_detail, name='meal_detail'),
]
