# litreview/views.py

from itertools import chain
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tickets.models import Ticket
from review.models import Review
from follows.models import UserFollows 

@login_required
def feed_view(request):
    # 1. Récupérer les utilisateurs suivis + soi-même
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)
    users_to_display = list(followed_users) + [request.user.id]

    # 2. Filtrer tickets et critiques
    tickets = Ticket.objects.filter(user__id__in=users_to_display).annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(author__id__in=users_to_display).annotate(content_type=Value('REVIEW', CharField()))

    # 3. Fusionner et trier
    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed.html', {'posts': posts})


@login_required
def my_posts_view(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(request, 'my_posts.html', context)
