from django.urls import path
from .views import create_ticket, my_posts_view, edit_ticket, delete_ticket, ticket_detail

urlpatterns = [
    path('create/', create_ticket, name='create_ticket'),
    path('my-posts/', my_posts_view, name='my_posts'),
    path('edit/<int:ticket_id>/', edit_ticket, name='edit_ticket'),
    path('delete/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
    path('<int:ticket_id>/', ticket_detail, name='ticket_detail'),
]
