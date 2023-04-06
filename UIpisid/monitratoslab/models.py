# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alerta(models.Model):
    idalerta = models.AutoField(db_column='IDAlerta', primary_key=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='Hora')  # Field name made lowercase.
    sala = models.IntegerField(db_column='Sala', blank=True, null=True)  # Field name made lowercase.
    sensor = models.IntegerField(db_column='Sensor', blank=True, null=True)  # Field name made lowercase.
    leitura = models.DecimalField(db_column='Leitura', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipoalerta = models.CharField(db_column='TipoAlerta', max_length=20)  # Field name made lowercase.
    mensagem = models.CharField(db_column='Mensagem', max_length=100)  # Field name made lowercase.
    horaescrita = models.DateTimeField(db_column='HoraEscrita')  # Field name made lowercase.
    idexperiencia = models.IntegerField(db_column='IDExperiencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alerta'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experiencia(models.Model):
    idexperiencia = models.AutoField(db_column='IDExperiencia', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase.
    investigador = models.CharField(db_column='Investigador', max_length=50)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora')  # Field name made lowercase.
    numeroratos = models.IntegerField(db_column='NumeroRatos')  # Field name made lowercase.
    limiteratossala = models.IntegerField(db_column='LimiteRatosSala')  # Field name made lowercase.
    segundossemmovimento = models.IntegerField(db_column='SegundosSemMovimento')  # Field name made lowercase.
    temperaturaideal = models.DecimalField(db_column='TemperaturaIdeal', max_digits=4, decimal_places=2)  # Field name made lowercase.
    variacaotemperaturamaxima = models.DecimalField(db_column='VariacaoTemperaturaMaxima', max_digits=4, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'experiencia'


class Medicoespassagens(models.Model):
    idmedicao = models.AutoField(db_column='IDMedicao', primary_key=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='Hora')  # Field name made lowercase.
    salaentrada = models.IntegerField(db_column='SalaEntrada')  # Field name made lowercase.
    salasaida = models.IntegerField(db_column='SalaSaida')  # Field name made lowercase.
    idmongo = models.IntegerField(db_column='IDMongo')  # Field name made lowercase.
    idexperiencia = models.IntegerField(db_column='IDExperiencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicoespassagens'


class Medicoessalas(models.Model):
    idexperiencia = models.IntegerField(db_column='IDExperiencia', primary_key=True)  # Field name made lowercase.
    numeroratosfinal = models.IntegerField(db_column='NumeroRatosFinal')  # Field name made lowercase.
    sala = models.IntegerField(db_column='Sala')  # Field name made lowercase.
    hora = models.DateTimeField(db_column='Hora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicoessalas'
        unique_together = (('idexperiencia', 'sala'),)


class Medicoestemperatura(models.Model):
    idmedicao = models.AutoField(db_column='IDMedicao', primary_key=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='Hora')  # Field name made lowercase.
    leitura = models.DecimalField(db_column='Leitura', max_digits=4, decimal_places=2)  # Field name made lowercase.
    sensor = models.IntegerField(db_column='Sensor')  # Field name made lowercase.
    idmongo = models.IntegerField(db_column='IDMongo')  # Field name made lowercase.
    idexperiencia = models.IntegerField(db_column='IDExperiencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicoestemperatura'


class Odoresexperiencia(models.Model):
    sala = models.IntegerField(db_column='Sala', primary_key=True)  # Field name made lowercase.
    idexperiencia = models.ForeignKey(Experiencia, models.DO_NOTHING, db_column='IDExperiencia')  # Field name made lowercase.
    codigoodor = models.CharField(db_column='CodigoOdor', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odoresexperiencia'
        unique_together = (('sala', 'idexperiencia'),)


class Parametrosadicionais(models.Model):
    idexperiencia = models.ForeignKey(Experiencia, models.DO_NOTHING, db_column='IDExperiencia')  # Field name made lowercase.
    datahorainicio = models.DateTimeField(db_column='DataHoraInicio', blank=True, null=True)  # Field name made lowercase.
    datahorafim = models.DateTimeField(db_column='DataHoraFim', blank=True, null=True)  # Field name made lowercase.
    razaofim = models.TextField(db_column='RazaoFim', blank=True, null=True)  # Field name made lowercase.
    variosatributosalertasaadicionar = models.IntegerField(db_column='VariosAtributosAlertasAAdicionar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametrosadicionais'


class Substanciasexperiencia(models.Model):
    numeroratos = models.IntegerField(db_column='NumeroRatos')  # Field name made lowercase.
    codigosubstancia = models.CharField(db_column='CodigoSubstancia', primary_key=True, max_length=5)  # Field name made lowercase.
    idexperiencia = models.ForeignKey(Experiencia, models.DO_NOTHING, db_column='IDExperiencia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'substanciasexperiencia'
        unique_together = (('codigosubstancia', 'idexperiencia'),)


class Utilizador(models.Model):
    nomeutilizador = models.CharField(db_column='NomeUtilizador', max_length=100)  # Field name made lowercase.
    telefoneutilizador = models.CharField(db_column='TelefoneUtilizador', max_length=12)  # Field name made lowercase.
    tipoutilizador = models.CharField(db_column='TipoUtilizador', max_length=3)  # Field name made lowercase.
    emailutilizador = models.CharField(db_column='EmailUtilizador', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador'
