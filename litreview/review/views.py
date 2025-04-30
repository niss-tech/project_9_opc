from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Review, Ticket


@login_required
def create_review(request):
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
    review = get_object_or_404(Review, id=review_id, author=request.user)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('my_posts')
    return render(request, 'review/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)
    if request.method == "POST":
        review.delete()
        return redirect('my_posts')
    return render(request, 'review/delete_review.html', {'review': review})


@login_required
def create_review_for_ticket(request, ticket_id):
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
