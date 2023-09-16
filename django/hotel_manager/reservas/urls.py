from django.urls import path
from . import views

urlpatterns = [
    path('listar_quartos/', views.listar_quartos, name='listar_quartos'),
    path('reservar_quarto/<int:numero>/', views.reservar_quarto, name='reservar_quarto'),
    path('adicionar_quarto/', views.adicionar_quarto, name='adicionar_quarto'),
]
