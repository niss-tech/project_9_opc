from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from review.models import Review

@login_required
def create_ticket(request):
    form = TicketForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('feed')
    return render(request, 'tickets/create_ticket.html', {'form': form})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    form = TicketForm(request.POST or None, request.FILES or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('my_posts')
    return render(request, 'tickets/edit_ticket.html', {'form': form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == "POST":
        ticket.delete()
        return redirect('my_posts')
    return render(request, 'tickets/delete_ticket.html', {'ticket': ticket})

@login_required
def my_posts_view(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(author=request.user)

    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(request, 'tickets/my_posts.html', context)
