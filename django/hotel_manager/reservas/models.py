from django.db import models

class Quarto(models.Model):
    numero = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    data_reserva = models.DateField(blank=True, null=True)
    locatario = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.numero} - {self.disponivel} - {self.locatario}"