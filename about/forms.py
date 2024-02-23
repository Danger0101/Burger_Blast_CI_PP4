from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
            label='Email',
            required=True
        )
    phone_number = forms.CharField(
            label='Phone Number',
            required=True
        )
    message = forms.CharField(
            label='Message',
            widget=forms.Textarea,
            required=True
        )
