'''
This module contains views for the reservation app.
'''
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation


@login_required
def my_reservations(request):
    '''
    This view displays a list of reservations for the logged-in user.
    '''
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
        reservation.reservation_datetime = timezone.localtime(
            reservation.reservation_datetime
        )

    if not reservations:
        reservations = None

    return render(
        request,
        'reservation/my_reservations.html',
        {'reservations': reservations}
    )


@login_required
def make_reservation(request):
    '''
    This view allows the user to make a reservation.
    '''
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user

            # Combine date and time fields
            reservation_datetime = datetime.combine(
                form.cleaned_data['reservation_date'],
                form.cleaned_data['reservation_time']
            )
            # Make the datetime object timezone-aware
            reservation_datetime = timezone.make_aware(reservation_datetime)
            reservation.reservation_datetime = reservation_datetime

            reservation.save()
            return redirect('reservation:my_reservations')
    else:
        form = ReservationForm(user=request.user)

    return render(request, 'reservation/make_reservation.html', {'form': form})


@login_required
def edit_reservation(request, reservation_id):
    '''
    This view allows the user to edit a reservation.
    '''
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if not request.user.is_staff:
        if reservation.user != request.user:
            raise PermissionDenied("You don't have permission to edit this "
                                   "reservation.")

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save(commit=False)
            reservation_datetime = datetime.combine(
                form.cleaned_data['reservation_date'],
                form.cleaned_data['reservation_time']
            )
            # Make the datetime object timezone-aware
            reservation_datetime = timezone.make_aware(reservation_datetime)
            updated_reservation.reservation_datetime = reservation_datetime
            updated_reservation.save()
            return redirect('reservation:my_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation/edit_reservation.html', {'form': form})


@login_required
def delete_reservation(request, reservation_id):
    '''
    This view allows the user to delete a reservation.
    '''
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Check if the logged-in user is a staff member
    if not request.user.is_staff:
        if reservation.user != request.user:
            raise PermissionDenied("You don't have permission to delete this "
                                   "reservation.")

    # Delete the reservation
    reservation.delete()

    return redirect('reservation:my_reservations')
