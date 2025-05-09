from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import UserFollows
from .forms import FollowUserForm


@login_required
def follow_users_view(request):
    """
    Permet à un utilisateur de suivre un autre utilisateur via un formulaire.

    Args:
        request (HttpRequest): Requête HTTP contenant le formulaire
            et les informations de session.

    Returns:
        HttpResponse: Affiche la page des abonnements avec un formulaire
            de suivi et la liste des utilisateurs suivis.
    """
    form = FollowUserForm()
    message = ''

    if request.method == 'POST':
        form = FollowUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user_to_follow = User.objects.get(username=username)
                if user_to_follow == request.user:
                    message = "Vous ne pouvez pas vous suivre vous-même."
                else:
                    UserFollows.objects.get_or_create(
                        user=request.user,
                        followed_user=user_to_follow
                    )
                    return redirect('follow')
            except User.DoesNotExist:
                message = f"L'utilisateur '{username}' n'existe pas."

    followed_users = UserFollows.objects.filter(user=request.user)
    return render(
        request,
        'follows/follow.html',
        {
            'form': form,
            'followed_users': followed_users,
            'message': message
        }
    )


@login_required
def unfollow_user_view(request, follow_id):
    """
    Permet de se désabonner d’un utilisateur suivi.

    Args:
        request (HttpRequest): Requête HTTP envoyée par l’utilisateur connecté.
        follow_id (int): Identifiant du lien d’abonnement à supprimer.

    Returns:
        HttpResponseRedirect: Redirige vers la page des abonnements.
    """
    follow = get_object_or_404(
        UserFollows,
        id=follow_id,
        user=request.user
    )
    follow.delete()
    return redirect('follow')
