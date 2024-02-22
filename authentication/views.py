'''
Authentication views.
'''
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterUserForm,
    CustomUpdateUserForm,
    ChangeUserPasswordForm
)


def send_email(subject, message, recipient_list):
    '''
    Function to send plain text email.
    '''
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
    )


def register_user(request):
    """
    Handle user registration.
    """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user_email_subject = "Welcome to Our Website!"
            user_email_message = (
                f"Dear {first_name} {last_name},\n"
                f"Username: {username},\n\n"
                "Welcome to Our Website! We're excited to have you onboard.\n"
                "Thank you for registering with us.\n\n"
                "Best regards,\n"
                "The Team"
            )
            send_email(user_email_subject, user_email_message, [email])

            admin_email_subject = "New User Registered"
            admin_email_message = (
                f"New user registered with username: {username}"
            )
            send_email(
                admin_email_subject,
                admin_email_message,
                [settings.ADMIN_EMAIL]
            )

            login(request, user)
            messages.success(
                request, f"{username} registered successfully. Welcome!")
            return redirect('about:index')
        else:
            messages.error(
                request, "Invalid form data. Please check the form."
            )
            return render(request, "authentication/register.html", {
                'form': form
            })
    else:
        form = RegisterUserForm()
        return render(request, "authentication/register.html", {
            'form': form
        })


def login_user(request):
    """
    Handle user login.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('about:index')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "authentication/login.html", {})
    else:
        return render(request, "authentication/login.html", {})


def logout_user(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('about:index')


@login_required
def update_user(request):
    '''
    Update user information and password.
    '''
    user_form = CustomUpdateUserForm(
        request.POST or None,
        instance=request.user
    )
    password_form = ChangeUserPasswordForm(
        request.user,
        request.POST or None
    )

    if request.method == 'POST':
        if 'update_info' in request.POST and user_form.is_valid():
            user_form.save()
            username = request.user.username
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email
            subject = "Account Information Updated"
            message = (
                f"Dear {first_name} {last_name},\n"
                f"Username: {username},\n\n"
                "Your account information has been updated.\n\n"
                "Best regards,\n"
                "Burger Blast Team"
            )
            send_email(subject, message, [email])
            messages.success(request, "User information updated successfully.")
            return redirect('account:update')
        elif 'change_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            username = request.user.username
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email
            subject = "Password Changed"
            message = (
                f"Dear {first_name} {last_name},\n"
                f"Username: {username},\n\n"
                "Your password has been changed successfully.\n\n"
                "If you didn't perform this action, please contact us "
                "immediately.\n\n"
                "Best regards,\n"
                "Burger Blast Team"
            )
            send_email(subject, message, [email])
            messages.success(request, "Password changed successfully.")
            return redirect('account:update')

    return render(request, 'authentication/update_user.html', {
        'user_form': user_form,
        'password_form': password_form
    })
