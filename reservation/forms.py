from datetime import datetime, time, timedelta
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reservation


class ReservationForm(forms.ModelForm):
    '''
    The ReservationForm class is used to
    create a form for making a reservation.

    Attributes:
        reservation_date (DateField):
            The date of the reservation.
        reservation_time (TimeField):
            The time of the reservation.
        user (ForeignKey):
            The user who made the reservation.
        first_name (CharField):
            The first name of the person making the reservation.
        last_name (CharField):
            The last name of the person making the reservation.
        email (EmailField):
            The email address of the person making the reservation.
        party_size (PositiveIntegerField):
            The number of people in the party.
        phone_number (CharField):
            The phone number of the person making the reservation.
        special_requests (TextField):
            Any special requests for the reservation.
    '''
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    reservation_time = forms.TimeField(
        widget=forms.Select(choices=[]))

    class Meta:
        '''
        The Meta class is used to specify the model and fields for the form.
        '''
        model = Reservation
        fields = [
            'first_name', 'last_name',
            'email', 'reservation_date',
            'reservation_time', 'party_size',
            'phone_number', 'special_requests'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields['reservation_date'].widget.attrs['onchange'] = (
            'update_time_choices()'
        )
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
        if instance:
            self.fields['reservation_date'].initial = (
                instance.reservation_datetime.date()
            )
            self.fields['reservation_time'].initial = (
                instance.reservation_datetime.time()
            )

    class Media:
        '''
        Media class to add JavaScript files to the form.
        '''
        js = (
            'https://code.jquery.com/jquery-3.6.4.min.js',
            'reservation_form.js',
        )

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
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

        if not self.is_valid_reservation_date_time(
            reservation_date, reservation_time
        ):
            raise ValidationError("Invalid reservation date and time.")

    def is_valid_reservation_date_time(
        self, reservation_date, reservation_time
    ):
        '''
        Check if the reservation date and time are valid.

        Args:
            reservation_date (date): The date of the reservation.
            reservation_time (time): The time of the reservation.

        Returns:
            bool: True if the reservation date and time are valid,
                  False otherwise.
        '''
        # Get the current date and time in the project's timezone
        current_datetime = timezone.localtime(timezone.now())

        if reservation_date < current_datetime.date():
            return False

        if reservation_time is None:
            return False

        # Get the operating hours of the restaurant
        opening_time = time(10, 0)  # Restaurant opens at 10:00 AM
        closing_time = time(22, 0)  # Restaurant closes at 10:00 PM

        # Check if the reservation_time falls within operating hours
        if not (opening_time <= reservation_time <= closing_time):
            return False

        # Make reservation_datetime timezone-aware with the project's timezone
        reservation_datetime = timezone.make_aware(
            datetime.combine(reservation_date, reservation_time),
            timezone.get_current_timezone()
        )

        if reservation_datetime <= current_datetime + timedelta(minutes=30):
            return False

        # If all checks pass, return True
        return True
