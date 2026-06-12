from django import forms
from .models import Game, Screenshot

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('added_by', 'average_rating')