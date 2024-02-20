from django.urls import path
from .views import *

app_name = 'reservation'

urlpatterns = [
    path('make/', make_reservation, name='make_reservation'),
    path('my/', my_reservations, name='my_reservations'),
    path('<int:reservation_id>/edit/', edit_reservation, name='edit_reservation'),
    path('<int:reservation_id>/delete/', delete_reservation, name='delete_reservation'),
]
