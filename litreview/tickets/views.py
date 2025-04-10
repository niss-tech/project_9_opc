from django.shortcuts import render, redirect
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


