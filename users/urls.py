"""Defines URL patterns for users"""

from django.urls import path

from django.contrib.auth.views import redirect_to_login

from . import views


app_name = 'users'
urlpatterns = [
    # Login page.
    path('login/', {'template_name': 'users/login.html'},
         name='login'),
]
