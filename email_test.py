import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Set the Django settings module dynamically
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'burger_blast.settings')
django.setup()

# Send test email
send_mail(
    'Testing email',
    'This is a test email from Burger Blast project.',
    settings.DEFAULT_FROM_EMAIL,
    ['jhummel001@gmail.com'],
)
# Works in development environment
