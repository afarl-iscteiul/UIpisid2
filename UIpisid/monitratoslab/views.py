from datetime import datetime
from xmlrpc.client import DateTime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from .models import Experiencia, Utilizador, Parametrosadicionais, Odoresexperiencia, Substanciasexperiencia

import pymysql


# Create your views here.
def index(request):
    utilizador = selecionarutilizador(request)  # CARF - Pode estar numa session, menos pesquisas na base de dados
    experiencias = Experiencia.objects.filter(investigador=utilizador.emailutilizador).values('idexperiencia',
                                                                                              'datahora', 'descricao')
    if experiencias.count() > 0:
        flag = True
        for i in experiencias:
            id = i['idexperiencia']
            if flag:
                param_adicionais = Parametrosadicionais.objects.filter(idexperiencia=id).values('idexperiencia',
                                                                                                'datahorainicio',
                                                                                                'datahorafim',
                                                                                                'razaofim')
                flag = False
            else:
                param_adicionais |= Parametrosadicionais.objects.filter(idexperiencia=id).values('idexperiencia',
                                                                                                 'datahorainicio',
                                                                                                 'datahorafim',
                                                                                                 'razaofim')
    return render(request, 'monitratoslab/index.html',
                  {'param_adicionais': param_adicionais, 'experiencias': experiencias, 'utilizador': utilizador})


def autenticacao(request):
    return render(request, 'monitratoslab/autenticacao.html')


def teste(request):
    return render(request, 'monitratoslab/teste.html')


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
    fechtbd = conexaobd(request)
    salas = fechtbd[0][0]
    num_salas = list(range(1, salas + 1))
    context = {'num_salas': num_salas}
    if request.method == 'POST':
        numratos = request.POST.getlist('numratos[]')
        total_rats = sum([int(nr) for nr in numratos]) + int(request.POST['ratossemsubstancias'])

        if total_rats == int(request.POST['numeroratos']):

            experiencia = Experiencia()
            experiencia.descricao = request.POST['descricao']
            experiencia.investigador = request.user.email
            experiencia.datahora = datetime.now()
            experiencia.numeroratos = request.POST['numeroratos']
            experiencia.limiteratossala = request.POST['limiteratossala']
            experiencia.segundossemmovimento = request.POST['segundossemmovimento']
            experiencia.temperaturaideal = request.POST['temperaturaideal']
            experiencia.variacaotemperaturamaxima = request.POST['variacaotemperaturamaxima']
            experiencia.save()

            # ADICIONA SUBSTANCIA
            substancia = request.POST.getlist('substancia[]')
            numratos = request.POST.getlist('numratos[]')
            substanciasexperiencia = Substanciasexperiencia()
            substanciasexperiencia.idexperiencia = experiencia
            substanciasexperiencia.codigosubstancia = "Limpo"
            substanciasexperiencia.numeroratos = request.POST['ratossemsubstancias']

            for i in range(len(substancia)):
                substanciasexperiencia.codigosubstancia = substancia[i]
                substanciasexperiencia.numeroratos = numratos[i]
                substanciasexperiencia.idexperiencia = experiencia
                substanciasexperiencia.save()


            # FIM ADICIONA SUBSTANCIA
            for i in num_salas:
                odoresexperiencia = Odoresexperiencia()
                odoresexperiencia.sala = i
                odoresexperiencia.idexperiencia = experiencia
                odoresexperiencia.codigoodor = request.POST.get(f'sala_{i}', '')
                odoresexperiencia.save()

            #REGISTAR MODO DE ALERTAS
               # = request.POST['periodicidade']
               #  = request.POST['gravidade']



            return redirect('monitratoslab:detalheexperiencia', experiencia.idexperiencia)
        else:
            context['error_message'] = 'O número total de ratos deve corresponder ao número de ratos especificado para cada substância!'
            return render(request, 'monitratoslab/novaexperiencia.html', context)

    else:
        return render(request, 'monitratoslab/novaexperiencia.html', context)


def detalheexperiencia(request, experiencia_id):
    experiencia = get_object_or_404(Experiencia, pk=experiencia_id)
    context = {'experiencia': experiencia}
    return render(request, 'monitratoslab/detalheexperiencia.html', context)


def selecionarutilizador(request):
    mail_request_user = request.user.email
    utilizador = Utilizador.objects.get(emailutilizador__startswith=mail_request_user)
    return utilizador

# q = Experiencia(descricao = "estrato de hibisco", investigador = "adelade", datahora =timezone.now(), numeroratos = 10, limiteratossala = 20, segundossemmovimento = 5, temperaturaideal = 35, variacaotemperaturamaxima = 6)
# q.save()
# output = '<br>'.join([d.descricao for d in experiencias])
