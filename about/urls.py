from django.urls import path
from .views import index_view, about_view, contact_us

app_name = 'about'

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact-us/', contact_us, name='contact_us'),
]
