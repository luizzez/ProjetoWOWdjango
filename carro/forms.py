from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHomePage(forms.Form):
    email = forms.EmailField()

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ('username', 'email', 'password1', 'password2',)
        model = Usuario

