import uuid
from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
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
