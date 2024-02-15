from django.urls import path
from .views import index_view, about_view  # Import the about_view

app_name = 'about'

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
]
