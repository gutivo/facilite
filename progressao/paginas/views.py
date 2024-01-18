from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from django.shortcuts import get_object_or_404
from usuarios.models import Perfil

from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

import requests  # Importe a biblioteca requests para fazer requisições HTTP


from django.http import JsonResponse

from django.views import View

from bs4 import BeautifulSoup

import re


# Sua função para emitir certidões
def emitir_certidoes(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        certidoes_selecionadas = request.POST.getlist('certidoes')

        links = []

        for certidao in certidoes_selecionadas:
            api_url = f'https://api.infosimples.com/api/v2/consultas/{certidao}'
            api_token = 'ZLEgr0dzz6Ut35kDG2wDbiE6GqYADKROkuWg3siO'  # Substitua pelo seu token

            params = {
                'cnpj': cnpj,
                'cei': '',
                'token': api_token,
                'timeout': 600,
            }

            try:
                response = requests.post(api_url, data=params)
                response.raise_for_status()

                data = response.json()

                if data.get('code') == 200:
                    # Manipule os dados conforme necessário
                    # Aqui, estou adicionando a URL de site_receipts à lista de links
                    links.extend(data.get('site_receipts', []))
                else:
                    # Lida com erros da API
                    error_message = data.get('code_message', 'Erro desconhecido na API')
                    return JsonResponse({'error': error_message}, status=400)

            except requests.RequestException as e:
                # Lida com erros de requisição
                return JsonResponse({'error': f'Erro na requisição para a API: {str(e)}'}, status=500)

        # Redireciona para a página que exibe os links
        return JsonResponse({'success': True, 'links': links})

    return render(request, 'formulario.html')












def resultados_pesquisa(request):
    # Obtenha os parâmetros da pesquisa da solicitação GET
    termo_pesquisa = request.GET.get('nome', '')
    modulo = request.GET.get('modulo', 'licitacoes')
    formato = request.GET.get('formato', 'json')

    # Construa a URL da API de compras com base nos parâmetros da pesquisa
    url_api_compras = f'http://compras.dados.gov.br/{modulo}/v1/orgaos.{formato}?nome={termo_pesquisa}'

    try:
        # Faça uma solicitação à API de compras
        response = requests.get(url_api_compras)
        response.raise_for_status()  # Lança uma exceção para erros HTTP

        # Converta a resposta para JSON
        dados_resultado = response.json()

        # Renderize a página de resultados com os dados obtidos
        return render(request, 'resultados_pesquisa.html', {'dados_resultado': dados_resultado})

    except requests.exceptions.RequestException as e:
        # Lida com erros de requisição
        return HttpResponse(f'Ocorreu um erro: {e}', status=500)

class ComprasView(GroupRequiredMixin,LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    group_required = [u"administrador",u"colaborador"]
    template_name = "compras.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''
        
        return context  


    
    

class LoginView(TemplateView):
    template_name = "index.html"

class IndexView(TemplateView):
    template_name = "inicial.html"
    
class DashboadView(TemplateView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    template_name = "dashboard.html"
    group_required = [u"administrador"]




class SobreView(TemplateView):
    template_name = "sobre.html"    

class Minhatarefas(GroupRequiredMixin,LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    group_required = [u"administrador",u"colaborador", u"cliente"]
    template_name = "paineltarefas.html"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Obtém o perfil associado ao usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)

        # Adiciona a URL da foto ao contexto
        context['foto'] = perfil.foto.url if perfil.foto else ''
        
        return context  