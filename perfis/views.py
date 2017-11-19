from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from perfis.models import Perfil, Convite

@login_required
def index(request):
	perfil_logado = get_perfil_logado(request)
	return render(request, 'index.html', { 'perfil_logado' : perfil_logado })

@login_required
def listar(request):
	perfis = Perfil.objects.all()
	perfil_logado = get_perfil_logado(request)
	return render(request, 'perfis.html', { 'perfis' : perfis, 'perfil_logado' : perfil_logado })

@login_required
def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	is_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html', { 'perfil' : perfil, 'perfil_logado' : perfil_logado, 'is_contato' : is_contato })

@login_required
def convidar(request, perfil_id):
	perfil_convidar = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidar)
	return redirect('listar')

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('listar')

@login_required
def get_perfil_logado(request):
	return request.user.perfil