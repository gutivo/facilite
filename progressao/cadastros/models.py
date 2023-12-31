from django.db import models
from django.contrib.auth.models import User
import datetime

class Campo(models.Model):
    nome = models.CharField(max_length=50,verbose_name="Órgão/Empresa")
    descricao = models.CharField(max_length=150,verbose_name="Descrição")
    foto = models.ImageField(upload_to='imagens/')
    def __str__(self):
     return "{} - ({}) {}".format(self.nome, self.descricao, self.foto)
# Create your models here.

class Atividade(models.Model):
    STATUS_CHOICES = [
        ('A receber', 'A receber'),
        ('Recebido', 'Recebido'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelada', 'Cancelada'),
    ]

    numero = models.CharField(max_length=150, verbose_name="Atribuição")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data de Referência", default=datetime.date.today)
    prazo = models.DateField(verbose_name="Prazo Final", default=datetime.date.today)
    colaborador = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Colaborador", null=True)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, verbose_name="Órgão/Empresa")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='A receber')
    arquivo = models.FileField(upload_to='pdf/',verbose_name="Anexos",blank=True)  
   
    
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.numero, self.descricao, self.colaborador,self.campo.nome, self.status,self.campo.foto)

class AtividadeLeitura(Atividade):
  
    class Meta:
        proxy = True  # Isso cria um modelo proxy para a leitura, compartilhando a tabela com o modelo original

    readonly_fields = ['numero', 'descricao', 'data', 'prazo', 'colaborador', 'campo', 'status']
    @property
    def fotoorgao(self):
        return self.campo.foto.url if self.campo.foto else ''
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.numero, self.descricao, self.data, self.prazo, self.colaborador, self.campo.nome, self.fotoorgao)
    
class Comentario(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(blank=True)
    arquivo = models.FileField(upload_to='comentarios/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário por {self.autor.username} em {self.data_publicacao}"