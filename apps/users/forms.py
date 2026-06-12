from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'username', 'password']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }