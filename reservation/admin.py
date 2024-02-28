from django.contrib import admin
from .models import Reservation
from .views import (
    send_reservation_confirmation_email,
    send_reservation_update_confirmation_email
)
from django.core.mail import send_mail
from django.conf import settings

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
    actions = (
        'send_reservation_confirmation',
        'send_reservation_update',
        'send_cancel_email_to_user'
    )

    def send_reservation_confirmation(self, request, queryset):
        for reservation in queryset:
            send_reservation_confirmation_email(reservation)
        self.message_user(
            request,
            "Reservation confirmation emails sent successfully."
        )

    send_reservation_confirmation.short_description = (
        "Send confirmation email for selected reservations"
    )

    def send_reservation_update(self, request, queryset):
        for reservation in queryset:
            send_reservation_update_confirmation_email(reservation)
        self.message_user(
            request,
            "Reservation update emails sent successfully."
        )

    send_reservation_update.short_description = (
        "Send update email for selected reservations"
    )

    def send_cancel_email_to_user(self, request, queryset):
        for reservation in queryset:
            # Assuming you want to send the email here
            send_custom_cancel_email_to_user({
                'first_name': reservation.first_name,
                'last_name': reservation.last_name,
                'datetime': reservation.reservation_datetime,
                'confirmation_number': reservation.confirmation_number,
                'user': reservation.user
            })
        self.message_user(
            request,
            "Reservation cancellation emails sent successfully."
        )

    send_cancel_email_to_user.short_description = (
        "Send cancellation email for selected reservations"
    )

def send_custom_cancel_email_to_user(deleted_reservation_details):
    '''
    Send cancellation email to user (if staff member deletes reservation).
    '''
    subject = 'Reservation Cancellation'
    message = (
        f"Dear {deleted_reservation_details['first_name']} "
        f"{deleted_reservation_details['last_name']},\n\n"
        "We regret to inform you that due to unforeseen"
        " circumstances, your reservation has been cancelled."
        " Please reach out to us if you require further assistance"
        " or to make a new reservation.\n\n"
        "Reservation Details:\n"
        "Date & Time: "
        f"{deleted_reservation_details['datetime'].strftime(
            '%B %d, %Y, %I:%M %p')}\n"
        "Confirmation Number:"
        f"{deleted_reservation_details['confirmation_number']}\n\n"
        "Thank you for your understanding.\n\n"
        "Sincerely,\nBurger Blast Team"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [deleted_reservation_details['user'].email]
    )

admin.site.register(Reservation, ReservationAdmin)
