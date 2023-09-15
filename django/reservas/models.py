from django.db import models

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
