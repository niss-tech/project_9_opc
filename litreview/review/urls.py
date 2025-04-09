from django.urls import path
from .views import create_review

urlpatterns = [
    path('create/', create_review, name='create_review'),
]
