'''
This file is used to register the Reservation model with the admin site.
'''
from django.contrib import admin
from .models import Reservation

admin.site.register(Reservation)
