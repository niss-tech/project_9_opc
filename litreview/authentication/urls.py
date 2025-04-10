# authentication/urls.py

from django.urls import path
from .views import signup_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup_view, landing_view
from .views import signup_view, landing_view

urlpatterns = [
    path('', landing_view, name='landing'),
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),
]