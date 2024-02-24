'''
This module contains views for the reservation app.
'''
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation


@login_required
def my_reservations(request):
    '''
    This view displays a list of future reservations for the logged-in user.
    '''
    # Get the current time
    now = timezone.now()

    # Filter reservations based on user type
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

    # Filter out past reservations
    reservations = reservations.filter(reservation_datetime__gte=now)

    # Convert reservation datetime to the user's timezone
    for reservation in reservations:
        reservation.reservation_datetime = timezone.localtime(
            reservation.reservation_datetime
        )

    # Pagination
    paginator = Paginator(reservations, 5)
    page = request.GET.get('page')
    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reservations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        reservations = paginator.page(paginator.num_pages)

    if not reservations:
        no_reservations_message = "You have no future reservations at the moment."
        return render(
            request,
            'reservation/my_reservations.html',
            {'no_reservations_message': no_reservations_message}
        )

    return render(
        request,
        'reservation/my_reservations.html',
        {'reservations': reservations, 'now': now}
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

            # Send reservation confirmation email
            send_reservation_confirmation_email(reservation)

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

    # Check permission to edit reservation
    if not request.user.is_staff and reservation.user != request.user:
        raise PermissionDenied("You don't have permission to edit "
                               "this reservation.")

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

            # Send reservation update confirmation email
            send_reservation_update_confirmation_email(updated_reservation)

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

    # Check permission to delete reservation
    if not request.user.is_staff and reservation.user != request.user:
        raise PermissionDenied("You don't have permission to delete "
                               "this reservation.")

    # Save reservation details before deletion
    deleted_reservation_details = {
        'datetime': timezone.localtime(reservation.reservation_datetime),
        'user': reservation.user,
        'first_name': reservation.first_name,
        'last_name': reservation.last_name,
        'confirmation_number': reservation.confirmation_number
    }

    # Send email based on who is deleting the reservation
    if request.user.is_staff:
        send_cancel_email_to_user(deleted_reservation_details)
    else:
        send_confirmation_email_to_user(deleted_reservation_details)

    # Delete the reservation
    reservation.delete()
    return redirect('reservation:my_reservations')


def send_reservation_confirmation_email(reservation):
    '''
    Send reservation confirmation email to user.
    '''
    subject = 'Reservation Confirmation'
    message = (
        f"Dear {reservation.first_name} {reservation.last_name},\n\n"
        "We have successfully received your reservation.\n\n"
        "Reservation Details:\n"
        f"Date & Time: {reservation.reservation_datetime.strftime('%B %d, %Y, %I:%M %p')}\n"
        f"Party Size: {reservation.party_size}\n"
        f"Confirmation Number: {reservation.confirmation_number}\n\n"
        f"Phone Number: {reservation.phone_number}\n"
        f"Special Requests: {reservation.special_requests}\n\n"
        "Thank you for choosing our restaurant.\n\n"
        "Best regards,\nBurger Blast Team"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [reservation.user.email])


def send_reservation_update_confirmation_email(updated_reservation):
    '''
    Send reservation update confirmation email to user.
    '''
    subject = 'Reservation Update Confirmation'
    message = (
        f"Dear {updated_reservation.first_name} {updated_reservation.last_name},\n\n"
        "We have successfully updated your reservation.\n\n"
        "Updated Reservation Details:\n"
        f"Date & Time: {updated_reservation.reservation_datetime.strftime('%B %d, %Y, %I:%M %p')}\n"
        f"Confirmation Number: {updated_reservation.confirmation_number}\n\n"
        f"Party Size: {updated_reservation.party_size}\n"
        f"Phone Number: {updated_reservation.phone_number}\n"
        f"Special Requests: {updated_reservation.special_requests}\n\n"
        "Thank you for choosing our restaurant.\n\n"
        "Best regards,\nBurger Blast Team"
    )

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [updated_reservation.user.email])


def send_cancel_email_to_user(deleted_reservation_details):
    '''
    Send cancellation email to user (if staff member deletes reservation).
    '''
    subject = 'Reservation Cancellation'
    message = (
        f"Dear {deleted_reservation_details['first_name']} "
        f"{deleted_reservation_details['last_name']},\n\n"
        "We regret to inform you that due to unforeseen circumstances, your reservation has been cancelled."
        "Please reach out to us if you require further assistance or to make a new reservation.\n\n"
        "Reservation Details:\n"
        f"Date & Time: {deleted_reservation_details['datetime'].strftime('%B %d, %Y, %I:%M %p')}\n"
        f"Confirmation Number: {deleted_reservation_details['confirmation_number']}\n\n"
        "Thank you for your understanding.\n\n"
        "Sincerely,\nBurger Blast Team"
    )

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [deleted_reservation_details['user'].email])


def send_confirmation_email_to_user(deleted_reservation_details):
    '''
    Send confirmation email to user (if user deletes their own reservation).
    '''
    subject = 'Reservation Deletion Confirmation'
    message = (
        f"Dear {deleted_reservation_details['first_name']} {deleted_reservation_details['last_name']},\n\n"
        "We would like to confirm that your reservation has been successfully cancelled.\n\n"
        "Reservation Details:\n"
        f"Date & Time: {deleted_reservation_details['datetime'].strftime('%B %d, %Y, %I:%M %p')}\n"
        f"Time: {deleted_reservation_details['datetime'].strftime('%I:%M %p')}\n"
        f"Confirmation Number: {deleted_reservation_details['confirmation_number']}\n\n"
        "If you have any questions or need further assistance, please don't hesitate to contact us.\n\n"
        "Best regards,\nBurger Blast Team"
    )

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [deleted_reservation_details['user'].email])
