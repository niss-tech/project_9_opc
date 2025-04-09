# litreview/views.py

from itertools import chain
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tickets.models import Ticket
from review.models import Review

@login_required
def feed_view(request):
    tickets = Ticket.objects.all().annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.all().annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'feed.html', {'posts': posts})
