# -*- coding: utf-8 -*-
from django.db import models
from institucion.models import Ciclo
from alumno.models import Alumno
from pago.models import Monto

TIPO_TURNO = (
    ('1', 'Mañana'),
    ('2', 'Tarde'),
    ('3', 'Noche'),
)

class Campus(models.Model):
    ciclo        = models.ForeignKey(Ciclo)
    seccion      = models.CharField('Sección',max_length=10)
    ano          = models.IntegerField('Año')
    semestre     = models.IntegerField('Semestre')
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_fin    = models.DateField('Fecha de Fin')
    turno        = models.CharField('Turno',max_length=2, choices=TIPO_TURNO)

    def __unicode__(self):
        return u'%s - %s' % (self.turno,self.seccion)

class AlumnosCampus(models.Model):
    alumno = models.ForeignKey(Alumno)
    campus = models.ForeignKey(Campus)
    monto  = models.ForeignKey(Monto)
