from django import forms
from .models import Quarto

class ReservaForm(forms.Form):
    nome_locatario = forms.CharField(max_length=100)
    data_reserva = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['numero', 'disponivel']