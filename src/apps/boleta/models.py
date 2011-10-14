# -*- coding: utf-8 -*-
from django.db import models
from alumno.models import Alumno

class Boleta(models.Model):
    alumno        = models.ForeignKey(Alumno)
    serie         = models.CharField('Serie', max_length=3)
    numero        = models.CharField('Número', max_length=7)
    concepto      = models.CharField('Concepto', max_length=250)
    fecha_emision = models.DateTimeField('Fecha de emisión', )
    valido        = models.BooleanField('¿Valida?', default=True)
    monto         = models.DecimalField('Monto', max_digits=8,decimal_places=1)
    saldo         = models.DecimalField('Saldo', max_digits=8,decimal_places=1)
    observacion   = models.TextField('Observación', blank=True,null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.serie,self.numero)
