from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Review, Ticket


@login_required
def create_review(request):
    """
    Permet à l’utilisateur de créer une critique indépendante.

    Args:
        request (HttpRequest): Requête de l’utilisateur (GET ou POST).

    Returns:
        HttpResponse: Affiche un formulaire vide ou redirige vers le flux
        si la critique a été créée avec succès.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('feed')
    else:
        form = ReviewForm()
    return render(request, 'review/create_review.html', {'form': form})


@login_required
def edit_review(request, review_id):
    """
    Permet de modifier une critique existante de l’utilisateur.

    Args:
        request (HttpRequest): Requête contenant les modifications éventuelles.
        review_id (int): ID de la critique à modifier.

    Returns:
        HttpResponse: Formulaire de modification ou redirection vers "my_posts"
        après validation.
    """
    review = get_object_or_404(Review, id=review_id, author=request.user)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('my_posts')
    return render(request, 'review/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    """
    Permet de supprimer une critique créée par l’utilisateur.

    Args:
        request (HttpRequest): Requête GET ou POST.
        review_id (int): ID de la critique à supprimer.

    Returns:
        HttpResponse: Affiche une page de confirmation ou redirige après
        suppression.
    """
    review = get_object_or_404(Review, id=review_id, author=request.user)
    if request.method == "POST":
        review.delete()
        return redirect('my_posts')
    return render(request, 'review/delete_review.html', {'review': review})


@login_required
def create_review_for_ticket(request, ticket_id):
    """
    Crée une critique en réponse à un ticket existant.

    Args:
        request (HttpRequest): Requête GET ou POST.
        ticket_id (int): ID du ticket auquel on veut répondre.

    Returns:
        HttpResponse: Affiche le formulaire ou redirige vers le flux si la
        critique est enregistrée.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.ticket = ticket
        review.save()
        return redirect('feed')
    return render(
        request,
        'review/create_review_for_ticket.html',
        {'form': form, 'ticket': ticket}
    )
