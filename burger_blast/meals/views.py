from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Meal

# Define a test function to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def create_or_update_meal(request, meal_id=None):
    if meal_id:
        meal = get_object_or_404(Meal, pk=meal_id)
    else:
        meal = Meal()

    if request.method == 'POST':
        meal.name = request.POST['name']
        meal.description = request.POST['description']
        meal.people = request.POST['people']
        meal.price = request.POST['price']
        meal.image = request.POST['image']
        meal.calories = request.POST['calories']
        meal.allergens = request.POST['allergens']
        meal.preparation_time = request.POST['preparation_time']
        meal.slug = request.POST['slug']


    meal.save()
    return render(request, 'menu_edit.html', {'meal': meal})
