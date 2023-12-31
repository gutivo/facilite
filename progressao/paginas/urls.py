from django.urls import path
from .views import IndexView,SobreView,LoginView,Minhatarefas,DashboadView,ComprasView
from .views import resultados_pesquisa
from .views import emitir_certidoes

urlpatterns = [ 
    path('',IndexView.as_view(), name ='inicio'),
    path('sobre/',SobreView.as_view(), name ='sobre'),
    path('tarefas/',Minhatarefas.as_view(), name ='tarefas'),
    path('compras/',ComprasView.as_view(), name ='compras'),
    path('resultados_pesquisa/', resultados_pesquisa, name='resultados_pesquisa'),
    path('emitir_certidoes/', emitir_certidoes, name='emitir_certidoes'),

]