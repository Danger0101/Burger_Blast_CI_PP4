'''
This file is used to register the Reservation model with the admin site.
'''
from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'reservation_datetime',
        'confirmation_number',
        'party_size',
        'phone_number'
    )
    list_filter = ('reservation_datetime', 'party_size')
    search_fields = (
        'user__username',
        'first_name',
        'last_name',
        'email',
        'phone_number'
    )
    readonly_fields = ('confirmation_number',)
    fieldsets = (
        (None, {
            'fields': ('user', 'reservation_datetime', 'confirmation_number')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Reservation Details', {
            'fields': ('party_size', 'special_requests'),
        }),
    )


admin.site.register(Reservation, ReservationAdmin)
