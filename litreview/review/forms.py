from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body']
        widgets = {
            'rating': forms.RadioSelect(
                choices=[
                    (i, str(i)) for i in range(1, 6)
                ]
            ),
        }
