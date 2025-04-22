from django.urls import path
from .views import create_review, edit_review, delete_review, create_review_for_ticket

urlpatterns = [
    path('create/', create_review, name='create_review'),
    path('create/<int:ticket_id>/', create_review_for_ticket, name='create_review_for_ticket'),
    path('edit/<int:review_id>/', edit_review, name='edit_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
]
