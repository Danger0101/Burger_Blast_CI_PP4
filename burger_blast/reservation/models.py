'''
The Reservation model is a simple model that
stores information about a reservation.
'''
import uuid
from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    '''
    The Reservation model stores information about a reservation.

    Attributes:
        user (ForeignKey):
            The user who made the reservation.
        reservation_datetime (DateTimeField):
            The date and time of the reservation.
        confirmation_number (str):
            The confirmation number for the reservation.
        first_name (str):
            The first name of the person making the reservation.
        last_name (str):
            The last name of the person making the reservation.
        email (EmailField):
            The email address of the person making the reservation.
        party_size (PositiveIntegerField):
            The number of people in the party.
        phone_number (str):
            The phone number of the person making the reservation.
        special_requests (TextField):
            Any special requests for the reservation.

    Methods:
        save:
            Overrides the save method to generate a
            confirmation number if one is not provided.
        __str__:
            Returns a string representation of the reservation.

    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_datetime = models.DateTimeField()
    confirmation_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True
        )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    party_size = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    special_requests = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_number:
            self.confirmation_number = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} "
            f"({self.email}) - {self.confirmation_number}"
        )
