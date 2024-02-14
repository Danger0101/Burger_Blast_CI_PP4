from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation


@login_required
def my_reservations(request):
    if request.user.is_staff:
        query = request.GET.get('q')
        if query:
            reservations = Reservation.objects.filter(
                Q(user__username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(reservation_datetime__icontains=query) |
                Q(confirmation_number__icontains=query)
            )
        else:
            reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user=request.user)

    # Convert reservation datetime to the user's timezone
    for reservation in reservations:
        reservation.reservation_datetime = timezone.localtime(reservation.reservation_datetime)

    if not reservations:
        reservations = None  # Set reservations to None if no reservations found

    return render(request, 'reservation/my_reservations.html', {'reservations': reservations})
