from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.models import User,Group
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil

class UsuarioCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = u"administrador"
    template_name="cadastros/form.html"
    form_class = UsuarioForm
    success_url=reverse_lazy('tarefas')

    def form_valid(self, form):
       grupo = get_object_or_404(Group, name="colaborador")
       
       url = super().form_valid(form)
       
       self.object.groups.add(grupo)
       self.object.save()
       
       # Cria um perfil associado ao usuário criado
       Perfil.objects.create(usuario=self.object)
       
       return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''

        context['titulo']= "Cadastro de Colaborador"
        context['buttao']= "Salvar"
        return context
    
class PerfilUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"administrador", u"colaborador"]
    template_name = "cadastros/form-upload.html"
    model = Perfil
    fields = ['nome_completo', 'telefone', 'foto']
    success_url = reverse_lazy('tarefas')

    def get_object(self, queryset=None): 
        # Obtém o perfil associado ao usuário logado
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''
        context['titulo'] = "Dados Perfil"
        context['buttao'] = "Alterar"
        return context