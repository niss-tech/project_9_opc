from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from review.models import Review


@login_required
def create_ticket(request):
    """
    Crée un nouveau ticket pour l'utilisateur connecté.

    Args:
        request (HttpRequest): Requête contenant les données du formulaire.

    Returns:
        HttpResponse: Redirection vers le feed ou page de création du ticket.
    """
    form = TicketForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('feed')
    return render(
        request,
        'tickets/create_ticket.html',
        {'form': form}
    )


@login_required
def edit_ticket(request, ticket_id):
    """
    Modifie un ticket existant appartenant à l'utilisateur.

    Args:
        request (HttpRequest): Requête contenant les données du formulaire.
        ticket_id (int): ID du ticket à modifier.

    Returns:
        HttpResponse: Page d'édition ou redirection vers mes publications.
    """
    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )
    form = TicketForm(
        request.POST or None,
        request.FILES or None,
        instance=ticket
    )
    if form.is_valid():
        form.save()
        return redirect('my_posts')
    return render(
        request,
        'tickets/edit_ticket.html',
        {'form': form}
    )


@login_required
def delete_ticket(request, ticket_id):
    """
    Supprime un ticket appartenant à l'utilisateur.

    Args:
        request (HttpRequest): Requête HTTP (GET ou POST).
        ticket_id (int): ID du ticket à supprimer.

    Returns:
        HttpResponse: Redirection après suppression ou page de confirmation.
    """
    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )
    if request.method == "POST":
        ticket.delete()
        return redirect('my_posts')
    return render(
        request,
        'tickets/delete_ticket.html',
        {'ticket': ticket}
    )


@login_required
def my_posts_view(request):
    """
    Affiche les tickets et critiques de l'utilisateur connecté.

    Args:
        request (HttpRequest): Requête HTTP.

    Returns:
        HttpResponse: Page affichant les posts personnels.
    """
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(author=request.user)

    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(
        request,
        'tickets/my_posts.html',
        context
    )


@login_required
def ticket_detail(request, ticket_id):
    """
    Affiche les détails d'un ticket et ses critiques associées.

    Args:
        request (HttpRequest): Requête HTTP.
        ticket_id (int): ID du ticket ciblé.

    Returns:
        HttpResponse: Page de détails du ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    reviews = Review.objects.filter(ticket=ticket)

    context = {
        'ticket': ticket,
        'reviews': reviews
    }
    return render(
        request,
        'tickets/ticket_detail.html',
        context
    )
