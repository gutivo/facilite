from django.urls import path
from .views import SuaVisualizacao


urlpatterns = [ 
  
    path('emitir_dispensa/',SuaVisualizacao.as_view(), name='emitir_dispensa'),

]