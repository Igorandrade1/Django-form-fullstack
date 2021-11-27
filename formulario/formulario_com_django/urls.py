from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^lista_pessoas/', lista_pessoas, name='lista_pessoas'),
    url(r'^cadastro_pessoas/', cadastro, name='cadastro'),
    url(r'^editar_cadastro/(?P<pk>[0-9]+)', editar_cadastro, name='editar_cadastro'),
    url(r'^remover_pessoa/(?P<pk>[0-9]+)', remover_pessoa, name='remover_pessoa'),
    url(r'^login/', login_user, name='login'),
    url(r'^logout', logout_user, name='logout'),
    

]
