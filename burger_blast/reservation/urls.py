from django.urls import path
from .views import *

app_name = 'reservation'

urlpatterns = [
    path('my/', my_reservations, name='my_reservations'),
]
