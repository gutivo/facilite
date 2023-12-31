from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Adicione um campo de relação para associar o perfil ao usuário
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    nome_completo = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=16, null=True)
    foto = models.ImageField(upload_to='imagens/')
   
# Create your models here.
