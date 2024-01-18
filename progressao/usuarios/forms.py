# forms.py
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=120)
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None, label='Grupo', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields  = ['username', 'email', 'password1', 'password2', 'grupo']

    def clean_grupo(self):
        grupo = self.cleaned_data['grupo']
        return grupo.id if grupo else None

