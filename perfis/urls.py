from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^perfis$', views.listar, name='listar'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    url(r'^convites/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar')
)