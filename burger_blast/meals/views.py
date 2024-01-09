from django.shortcuts import render
from .models import Meal

# Create your views here.
def meal_list(request):
    meal_list = Meal.objects.all()
    
    context = {
            'meal_list': meal_list,
    }
    
    render(request, 'meals/meal_list.html', {'meal_list': meal_list})

def meal_detail(request, slug):
    meal_detail = Meal.objects.get(slug=slug)
    
    render(request, 'meals/meal_detail.html', {'meal_detail': meal_detail})
