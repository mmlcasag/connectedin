from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite

def index(request):
	return render(request, 'index.html')

def listar(request):
	perfis = Perfil.objects.all()
	perfil_logado = get_perfil_logado(request)
	return render(request, 'perfis.html', { 'perfis' : perfis, 'perfil_logado' : perfil_logado })

def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	is_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html', { 'perfil' : perfil, 'is_contato' : is_contato })

def convidar(request, perfil_id):
	perfil_convidar = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidar)
	return redirect('listar')

def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('listar')
	
def get_perfil_logado(request):
	return Perfil.objects.get(id=1)