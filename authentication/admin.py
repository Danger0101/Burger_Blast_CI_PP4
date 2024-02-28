from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .views import send_email

def send_welcome_email(modeladmin, request, queryset):
    """
    Custom admin action to send welcome email to selected users.
    """
    for user in queryset:
        subject = "Welcome to Burger Blast!"
        message = (
            f"Dear {user.first_name} {user.last_name},\n"
            f"Username: {user.username},\n\n"
            "Welcome to Burger Blast! We're excited to have you onboard.\n"
            "Thank you for registering with us.\n"
            "You can now book reservations on the website.\n\n"
            "Best regards,\n"
            "The Burger Blast Team"
        )
        recipient_list = [user.email]
        send_email(subject, message, recipient_list)

send_welcome_email.short_description = _("Send welcome email to selected users")

def send_admin_notification(modeladmin, request, queryset):
    """
    Custom admin action to send admin notification for new user registration.
    """
    for user in queryset:
        subject = "New User Registered"
        message = f"New user registered with username: {user.username}"
        send_email(subject, message, [settings.ADMIN_EMAIL])

send_admin_notification.short_description = _("Send admin notification for new user registration")


def send_edit_notification(modeladmin, request, queryset):
    """
    Custom admin action to send notification when user information is edited.
    """
    for user in queryset:
        subject = "User Information Edited"
        message = (
            f"Dear {user.first_name} {user.last_name},\n"
            f"Username: {user.username},\n\n"
            "We have made the changes you've requested to your account.\n"
            "Please let us know if you need further assistance"
            " or have any questions or concerns about your account.\n\n"
            "Best regards,\n"
            "The Burger Blast Team"
        )
        send_email(subject, message, [user.email])

send_edit_notification.short_description = _("Send notification when user information is edited")

def send_delete_notification(modeladmin, request, queryset):
    """
    Custom admin action to send notification when user account is deleted.
    """
    for user in queryset:
        subject = "User Account Deleted"
        message = (
            f"Dear {user.first_name} {user.last_name},\n"
            f"Username: {user.username},\n\n"
            "We have deleted your account as requested or required.\n"
            "Please let us know if you need further assistance"
            " or have any questions or concerns about your account.\n\n"
            "Best regards,\n"
            "The Burger Blast Team"
        )
        send_email(subject, message, [user.email])

send_delete_notification.short_description = _("Send notification when user account is deleted")

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    actions = [
            send_welcome_email,
            send_admin_notification,
            send_edit_notification,
            send_delete_notification
        ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
