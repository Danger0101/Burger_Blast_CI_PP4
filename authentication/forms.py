'''
This file contains the forms for the authentication app. The forms are used to
create and update user accounts, and to change user passwords.
'''
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    '''
    The RegisterUserForm class is used to create a form for user registration.

    Attributes:
        email (EmailField):
            The email address of the user.
        first_name (CharField):
            The first name of the user.
        last_name (CharField):
            The last name of the user.
    '''
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        ),
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        ),
    )

    class Meta:
        '''
        The Meta class is used to specify the model and fields for the form.
        '''
        model = User
        fields = (
            "username", "first_name", "last_name", "email",
            "password1", "password2"
        )

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CustomUpdateUserForm(UserChangeForm):
    '''
    The CustomUpdateUserForm class is used to create a form for updating user
    information.

    Attributes:
        email (EmailField):
            The email address of the user.
    '''
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        ),
    )

    class Meta:
        '''
        The Meta class is used to specify the model and fields for the form.
        '''
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(CustomUpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class ChangeUserPasswordForm(PasswordChangeForm):
    '''
    The ChangeUserPasswordForm class is used to create a form for changing user
    passwords.

    Attributes:
        old_password (CharField):
            The user's old password.
        new_password1 (CharField):
            The user's new password.
        new_password2 (CharField):
            The user's new password confirmation.
    '''
    old_password = forms.CharField(
        label="Old Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
