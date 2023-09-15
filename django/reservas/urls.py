from django.urls import path
from . import views

urlpatterns = [
    path('fazer_reserva/', views.fazer_reserva, name='fazer_reserva'),
    path('listar_reservas/', views.listar_reservas, name='listar_reservas'),
]
