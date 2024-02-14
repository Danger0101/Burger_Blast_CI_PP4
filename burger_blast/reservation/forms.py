# burger_blast\reservation\forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time, timedelta
from .models import Reservation

class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    reservation_time = forms.TimeField(widget=forms.Select(choices=[]))

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'reservation_date', 'reservation_time', 'party_size', 'phone_number', 'special_requests']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Generate choices for the time field with 15-minute intervals within operating hours
        interval = 15
        self.fields['reservation_date'].widget.attrs['onchange'] = 'update_time_choices()'
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js', 'reservation_form.js',)

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')  # Changed from reservation_datetime
        reservation_time = cleaned_data.get('reservation_time')
        party_size = cleaned_data.get('party_size')

        if not reservation_date:
            raise ValidationError("Reservation date is required.")
        if not reservation_time:
            raise ValidationError("Reservation time is required.")
        if not party_size:
            raise ValidationError("Party size is required.")
        if party_size <= 0:
            raise ValidationError("Party size must be greater than zero.")

        if not self.is_valid_reservation_date_time(reservation_date, reservation_time):  # Changed from reservation_datetime
            raise ValidationError("Invalid reservation date and time.")

    def is_valid_reservation_date_time(self, reservation_date, reservation_time):  # Changed from reservation_datetime
        # Get the current date and time in the project's timezone
        current_datetime = timezone.localtime(timezone.now())

        # Ensure the reservation_date is in the future
        if reservation_date < current_datetime.date():
            return False

        # Check if reservation_time is not None
        if reservation_time is None:
            return False

        # Get the operating hours of the restaurant
        opening_time = time(10, 0)  # Assuming the restaurant opens at 10:00 AM
        closing_time = time(22, 0)  # Assuming the restaurant closes at 10:00 PM

        # Check if the reservation_time falls within operating hours
        if not (opening_time <= reservation_time <= closing_time):
            return False

        # Make reservation_datetime timezone-aware with the project's timezone
        reservation_datetime = timezone.make_aware(datetime.combine(reservation_date, reservation_time), timezone.get_current_timezone())  # Combine date and time

        # Check if the reservation_time is at least 30 minutes ahead from the current time
        if reservation_datetime <= current_datetime + timedelta(minutes=30):
            return False

        # Check if there are any conflicting reservations
        existing_reservations = Reservation.objects.filter(reservation_datetime=reservation_datetime)
        for existing_reservation in existing_reservations:
            if existing_reservation.reservation_datetime == reservation_datetime:
                return False

        # If all checks pass, return True
        return True
