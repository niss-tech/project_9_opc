from itertools import chain
from django.db.models import CharField, Value, Exists, OuterRef
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tickets.models import Ticket
from review.models import Review
from follows.models import UserFollows


@login_required
def feed_view(request):
    """
    Vue principale affichant le flux d’actualités de l’utilisateur connecté.

    Args:
        request (HttpRequest): Requête envoyée par un utilisateur connecté.

    Returns:
        HttpResponse: Page contenant les tickets et critiques des utilisateurs
        suivis ainsi que les siens, triés par date décroissante.
    """
    followed_users = UserFollows.objects.filter(
        user=request.user
    ).values_list('followed_user', flat=True)
    users_to_display = list(followed_users) + [request.user.id]

    tickets = Ticket.objects.filter(
        user__id__in=users_to_display
    ).annotate(
        has_review=Exists(
            Review.objects.filter(ticket=OuterRef('pk'))
        )
    ).annotate(content_type=Value('TICKET', CharField()))

    reviews = Review.objects.filter(
        author__id__in=users_to_display
    ).annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed.html', {'posts': posts})


@login_required
def my_posts_view(request):
    """
    Vue affichant uniquement les tickets et
    critiques de l’utilisateur connecté.

    Args:
        request (HttpRequest): Requête d’un utilisateur connecté.

    Returns:
        HttpResponse: Page listant les posts personnels (tickets + critiques).
    """
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(request, 'my_posts.html', context)
