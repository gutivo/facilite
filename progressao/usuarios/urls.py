from django.urls import path
from django.contrib.auth import views as auth_view
from .views import UsuarioCreate,PerfilUpdate

urlpatterns = [ 
 #   path('sobre/',SobreView.as_view(), name ='sobre'),
    path('login/', auth_view.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name= "login"),
    path('logout/', auth_view.LogoutView.as_view(),name="logout"),
    path('registrar/',UsuarioCreate.as_view(), name="registrar"),
    path('perfil/', PerfilUpdate.as_view(), name="perfil-atualizar"),
]