from django import forms
from .models import Comentario,Atividade

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'arquivo']

    def clean_texto(self):
        texto = self.cleaned_data['texto']
        if not texto.strip():  # Verifica se o comentário está vazio ou contém apenas espaços em branco
            raise forms.ValidationError("O comentário não pode estar vazio.")
        return texto
    

class StatusForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['arquivo','status']



