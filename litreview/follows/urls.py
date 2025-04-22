from django.urls import path
from .views import follow_users_view, unfollow_user_view

urlpatterns = [
    path('', follow_users_view, name='follow'),
    path('unfollow/<int:follow_id>/', unfollow_user_view, name='unfollow'),
]
