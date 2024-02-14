from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
        authenticate,
        login,
        logout
)
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterUserForm,
    CustomUpdateUserForm,
    ChangeUserPasswordForm
)


def register_user(request):
    """
    Handle user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the index.
    """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"{username} Registered successfully")
            return redirect('about:index')
        else:
            messages.error(request, "Invalid form data. "
                                    "Please check the form.")
            return render(request, "authentication/register.html", {
                'form': form
            })
    else:
        form = RegisterUserForm()
        return render(request, "authentication/register.html", {
            'form': form
        })
