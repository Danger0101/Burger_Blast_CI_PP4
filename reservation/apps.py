'''
The apps.py file is used to configure the reservation app.
'''
from django.apps import AppConfig


class ReservationConfig(AppConfig):
    '''
    The ReservationConfig class is used to configure the reservation app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'
