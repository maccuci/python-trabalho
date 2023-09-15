from django.shortcuts import render, redirect
from .models import Reserva
from datetime import datetime

reservas = []

def fazer_reserva(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_hora_str = request.POST.get('data_hora')
        try:
            data_hora = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
            reserva = Reserva(nome=nome, data_hora=data_hora)
            reservas.append(reserva)
        except ValueError:
            pass
        return redirect('listar_reservas')
    
def listar_reservas(request):
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})