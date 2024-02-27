'''
This module contains the views for the meals app.
'''
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from .models import Meal


def is_superuser(user):
    '''
    Check if the user is a superuser.

    Args:
        user (User): The user to check if they are a superuser.

    Returns:
        bool: True if the user is a superuser, False otherwise.
    '''
    return user.is_superuser


@user_passes_test(is_superuser)
def create_or_update_meal(request, meal_id=None):
    '''
    Create or update a meal.

    Args:
        request (HttpRequest): The request object.
        meal_id (int, optional): The ID of the meal to update.

    Returns:
        HttpResponse: The response object.
    '''
    if meal_id:
        meal = get_object_or_404(Meal, pk=meal_id)
    else:
        meal = Meal()

    if request.method == 'POST':
        meal.name = request.POST['name']
        meal.description = request.POST['description']
        meal.people = request.POST['people']
        meal.price = request.POST['price']
        meal.calories = request.POST['calories']
        meal.allergens = request.POST['allergens']
        meal.preparation_time = request.POST['preparation_time']
        meal.slug = request.POST['slug']

        meal.save()
        return render(request, 'menu_edit.html', {'meal': meal})
    else:
        return render(request, 'menu_edit.html', {'meal': meal})


def menu_view(request):
    '''
    Display the menu.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    context = {'active_page': 'menu'}
    meals = Meal.objects.all()
    return render(request, 'meals/menu.html', {'meals': meals})
