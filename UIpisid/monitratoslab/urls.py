from django.urls import include, path
from . import views

app_name = 'monitratoslab'
urlpatterns = [
    path("", views.index, name="index"),
    path('paginalogin', views.paginalogin, name='paginalogin'),
    path('paginalogout', views.paginalogout, name='paginalogout'),
    path('novaexperiencia/', views.novaexperiencia, name='novaexperiencia'),
    # path('detalheexperiencia/', views.detalheexperiencia, name='detalheexperiencia'),
    path('detalheexperiencia/<int:experiencia_id>/', views.detalheexperiencia, name='detalheexperiencia'),
    path('autenticacao', views.autenticacao, name='autenticacao'),
    path('teste', views.teste, name='teste'),


]