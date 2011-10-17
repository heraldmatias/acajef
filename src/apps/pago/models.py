from django.db import models
from boleta.models import Boleta

class Monto(models.Model):
    cantidad = models.IntegerField('Cantidad')
    deuda    = models.DecimalField('Deuda', max_digits=8,decimal_places=1)
    total    = models.DecimalField('Total', max_digits=8,decimal_places=1)

class Pension(models.Model):
    monto             = models.ForeignKey(Monto)
    total             = models.DecimalField('Total', max_digits=8,decimal_places=1)
    saldo             = models.DecimalField('Saldo', max_digits=8,decimal_places=1)
    fecha_vencimiento = models.DateField('Fecha de Vencimiento', auto_now=True)

class Pago(models.Model):
    pension = models.ForeignKey(Pension)
    boleta  = models.ForeignKey(Boleta)
