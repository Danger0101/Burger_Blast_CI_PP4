from django.urls import path
from .views import (
    make_reservation,
    my_reservations,
    edit_reservation,
    delete_reservation
)

app_name = 'reservation'

urlpatterns = [
    path('make/', make_reservation, name='make_reservation'),
    path('my/', my_reservations, name='my_reservations'),
    path(
        '<int:reservation_id>/edit/',
        edit_reservation,
        name='edit_reservation'
    ),
    path(
        '<int:reservation_id>/delete/',
        delete_reservation,
        name='delete_reservation'
    ),
]
