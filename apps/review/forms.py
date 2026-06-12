from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment', 'recommended')
        widgets = {
            'rating': forms.NumberInput(attrs={'min': '1', 'max': '5', 'step': '0.5'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Deixe sua opinião sobre o jogo aqui...'}),
        }