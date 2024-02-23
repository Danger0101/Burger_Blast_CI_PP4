'''
This module contains the views for the about app.
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm


def index_view(request):
    '''
    Renders the index page.
    '''
    context = {'active_page': 'index'}
    return render(request, 'about/index.html', context)


def about_view(request):
    '''
    Renders the about page.
    '''
    context = {'active_page': 'about'}
    return render(request, 'about/about.html', context)


def contact_us(request):
    '''
     View function to handle contact form submission.

    Upon receiving a POST request, this function validates the contact form,
    sends an email to the default email address with the submitted information,
    and redirects the user to the index page upon successful submission. If the
    form is not valid, it displays error messages to the user.

    Args:
        request:
            HttpRequest object containing the request data.

    Returns:
        HttpResponse:
            Renders the contact_us.html template with the contact form.
    '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            send_mail(
                'Contact Us Form Submission',
                f'Email: {email}\nPhone Number: '
                f'{phone_number}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'about/contact_us.html', {'form': form})