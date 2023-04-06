from datetime import datetime
from xmlrpc.client import DateTime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from .models import Experiencia, Utilizador, Parametrosadicionais

import pymysql


# Create your views here.
def index(request):
    experiencias = Experiencia.objects.all()
    utilizador = selecionarutilizador(request) # CARF - Pode estar numa session, menos pesquisas na base de dados
    param_adicionais = Parametrosadicionais.objects.all()

    exp = Experiencia.objects.get(pk=6)
    print(exp.idexperiencia)

    # x = exp.parametrosadicionais_set.all()
    # print(x)
    # z = Parametrosadicionais.objects.filter(experiencia__idexperiencia__exact=6)
    # print(z)

    return render(request, 'monitratoslab/index.html', {'experiencias':experiencias, 'utilizador':utilizador, 'param_adicionais':param_adicionais})


def paginalogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('monitratoslab:index'))
    if not request.method == 'POST':
        return render(request, 'monitratoslab/paginalogin.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('monitratoslab:index'))
    return HttpResponseRedirect(reverse('monitratoslab:paginalogin'))


def paginalogout(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect(reverse('monitratoslab:paginalogin'))

def novaexperiencia(request):
    if request.method == 'POST':
        experiencia = Experiencia()
        experiencia.descricao = request.POST['descricao']
        experiencia.investigador = request.POST['investigador']
        experiencia.datahora = datetime.now()
        experiencia.numeroratos = request.POST['numeroratos']
        experiencia.limiteratossala = request.POST['limiteratossala']
        experiencia.segundossemmovimento = request.POST['segundossemmovimento']
        experiencia.temperaturaideal = request.POST['temperaturaideal']
        experiencia.variacaotemperaturamaxima = request.POST['variacaotemperaturamaxima']
        experiencia.save()
        return redirect('experiencia_detail', pk=experiencia.idexperiencia)
    else:
        return render(request, 'monitratoslab/novaexperiencia.html')


def conexaobd(request):
    # CARF - Isto não é assim muito seguro
    conn = pymysql.connect(host="194.210.86.10", user="aluno", password="aluno")
    try:
        cursor = conn.cursor()
        cursor.execute("select numerosalas from pisid_2023_maze.configuraçãolabirinto")
        fetch = cursor.fetchall()
    finally:
        conn.close()
    return fetch


def selecionarutilizador(request):
    mail_request_user = request.user.email
    utilizador = Utilizador.objects.get(emailutilizador__startswith=mail_request_user)
    return utilizador


# fechtbd = conexaobd(request)
# num_salas = fechtbd[0][0]

# q = Experiencia(descricao = "estrato de hibisco", investigador = "adelade", datahora =timezone.now(), numeroratos = 10, limiteratossala = 20, segundossemmovimento = 5, temperaturaideal = 35, variacaotemperaturamaxima = 6)
# q.save()
# output = '<br>'.join([d.descricao for d in experiencias])