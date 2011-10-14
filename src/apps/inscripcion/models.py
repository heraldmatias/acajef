# -*- coding: utf-8 -*-
from django.db import models

"""
App for Inscripcion
"""

TIPO_CARRERA = (
    ('1', 'Mensual'),
    ('2', 'Semanal'),
    ('3', 'Día'),
)

TIPO_TURNO = (
    ('1', 'Mañana'),
    ('2', 'Tarde'),
    ('3', 'Noche'),
)

class Carrera(models.Model):
    carrera  = models.CharField('Carrera',max_length=150)
    duracion = models.IntegerField('Dureción')
    tipo     = models.CharField('Tipo',max_length=2, choices=TIPO_CARRERA)
    monto    = models.DecimalField('Monto',max_digits=8,decimal_places=1)
    valido   = models.BooleanField('¿Valida?',default=False)

    def __unicode__(self):
        return u'%s' % (self.carrera)

class Ciclo(models.Model):
    carrera = models.ForeignKey(Carrera)
    ciclo   = models.CharField('Ciclo',max_length=100)

    def __unicode__(self):
        return u'%s' % self.ciclo


