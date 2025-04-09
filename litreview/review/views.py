from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

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
