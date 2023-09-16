from django.shortcuts import render, redirect
from .models import Quarto
from .forms import ReservaForm, QuartoForm

quartos = []

def adicionar_quarto(request):
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            form.save()
            quartos.append(form.instance)
            return redirect('listar_quartos')
    else:
        form = QuartoForm()
    return render(request, 'reservas/adicionar_quarto.html', {'form': form})

def listar_quartos(request):
    return render(request, 'reservas/listar_quartos.html', {'quartos': quartos})

def reservar_quarto(request, numero):
    quarto = next((q for q in quartos if q.numero == numero), None)
    if quarto and quarto.disponivel:
        if request.method == 'POST':
            form = ReservaForm(request.POST)
            if form.is_valid():
                nome_locatario = form.cleaned_data['nome_locatario']
                data_reserva = form.cleaned_data['data_reserva']
                quarto.disponivel = False
                quarto.locatario = nome_locatario
                quarto.data_reserva = data_reserva
                return redirect('listar_quartos')
        else:
            form = ReservaForm()
        return render(request, 'reservas/reservar_quarto.html', {'quarto': quarto, 'form': form})
    else:
        return redirect('listar_quartos')