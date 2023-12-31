from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.views.generic import ListView
from django.db.models import Count
from .models import Atividade

from django.shortcuts import get_object_or_404
from usuarios.models import Perfil
    
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ComentarioForm   

from django.utils.safestring import mark_safe


########### INSERT ###############
class CampoCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Campo
    fields = ['nome','descricao','foto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''


        context['titulo']= "Cadastramento de Órgão/Empresa"
        context['buttao']= "Salvar"
        return context

class AtividadeCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):    
 login_url = reverse_lazy('login')
 group_required = u"administrador"
 model = Atividade
 fields = ['numero','descricao','data','prazo','colaborador','campo','status','arquivo']
 template_name = 'cadastros/form-upload.html'
 success_url = reverse_lazy('listar-atividades')

 def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''


        context['titulo']= "Cadastramento de atividade"
        context['buttao']= "Salvar"
        return context

 ########## UPDATE #################

class CampoUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Campo
    fields = ['nome','descricao','foto']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''


        context['titulo']= "Alteração"
        context['buttao']= "Alterar"
        return context


class AtividadeUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):    
 login_url = reverse_lazy('login')
 group_required = u"administrador"
 model = Atividade
 fields = ['numero','descricao','data','prazo','colaborador','campo','status','arquivo']
 template_name = 'cadastros/form-upload.html'
 success_url = reverse_lazy('listar-atividades')


 def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''

        context['titulo']= "Alteração de Atividade"
        context['buttao']= "Alterar"
        return context
 #######CCOLABORADOR

class AtividadeLeitura(GroupRequiredMixin, LoginRequiredMixin, UpdateView):    
    login_url = reverse_lazy('login')
    group_required = [u"administrador",u"colaborador"]
    model = Atividade
    readonly_fields = ['numero', 'descricao', 'data', 'prazo', 'colaborador', 'campo']
    fields = ['arquivo','status']
    template_name = 'cadastros/formabrir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)
        
        context['foto'] = perfil.foto.url if perfil.foto else ''
        
         # Acesse o campo associado ao modelo AtividadeLeitura
        campo_da_atividade_leitura = self.object.campo
        context['fotoorgao'] = campo_da_atividade_leitura.foto.url if campo_da_atividade_leitura.foto else ''

        # Adicione o formulário de comentários ao contexto
        context['comentario_form'] = ComentarioForm()

        return context
    
   
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST, request.FILES)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.atividade = self.object
            comentario.autor = self.request.user
            comentario.save()
            return HttpResponseRedirect(self.get_success_url())

        # Se o formulário não for válido, re-renderize a página com o formulário de comentários
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST, request.FILES)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.atividade = self.object
            comentario.autor = self.request.user
            comentario.save()
            return HttpResponseRedirect(self.get_success_url())

        # Se o formulário não for válido, re-renderize a página com o formulário de comentários
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    
 ############## DELETE #################

class CampoDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''
        return context

class AtividadeDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):    
 login_url = reverse_lazy('login')
 group_required = u"administrador"
 model = Atividade
 template_name = 'cadastros/form-excluir.html'
 success_url = reverse_lazy('listar-atividades')

 def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''
        return context
 
############## LISTA ################

class CampoList(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = u"administrador"
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''
        return context

class AtividadeList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'    
    context_object_name = 'atividades'
    

    def get_queryset(self):
        queryset = Atividade.objects.all()

        # Filtrar por status
        status = self.request.GET.get('status', None)
        if status:
            queryset = queryset.filter(status=status)

        # Filtrar por data (mes e ano)
        mes = self.request.GET.get('mes', None)
        ano = self.request.GET.get('ano', None)
        if mes and ano:
            queryset = queryset.filter(data__month=mes, data__year=ano)

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        context['foto'] = perfil.foto.url if perfil.foto else ''
        return context
    

class DashList(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = u"administrador"
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'dashboard.html'
    context_object_name = 'atividades'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''


        # Dados para o gráfico de coluna (quantidades de cada mês)
        context['quantidades_por_mes'] = Atividade.objects.values('data__month').annotate(quantidade=Count('id'))

        # Dados para o gráfico de pizza (quantidade de tarefas por status)
        context['quantidades_por_status'] = Atividade.objects.values('status').annotate(quantidade=Count('id'))

        # Dados para o gráfico de barra (quantidade de tarefas por campo)
        context['quantidades_por_campo'] = Atividade.objects.values('campo__nome').annotate(quantidade=Count('id'))

        return context
    
    
    

    
  
   

    



    