# -*- coding: utf-8 -*-
from django.db import models
from boleta.models import Boleta

"""
App for Pago
"""

class Monto(models.Model):
    deuda     = models.DecimalField('Deuda', max_digits=8,decimal_places=1)
    total     = models.DecimalField('Total', max_digits=8,decimal_places=1)
    n_pension = models.IntegerField('N° de pensiones pagadas', blank=True, null=True)
    n_pago    = models.IntegerField('N° de pensiones pagadas', blank=True, null=True)

class Pension(models.Model):
    monto             = models.ForeignKey(Monto)
    total             = models.DecimalField('Total', max_digits=8,decimal_places=1)
    saldo             = models.DecimalField('Saldo', max_digits=8,decimal_places=1)
    fecha_vencimiento = models.DateField('Fecha de Vencimiento', auto_now=True)

class Pago(models.Model):
    pension = models.ForeignKey(Pension)
    boleta  = models.ForeignKey(Boleta)
