# listings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
]

