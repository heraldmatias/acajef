# -*- coding: utf-8 -*-
from django.db import models
from institucion.models import Ciclo
from alumno.models import Alumno
from concepto.models import Concepto

"""
App for Campus
"""

TURNO = (
    (0, 'Mañana'),
    (1, 'Tarde'),
    (2, 'Noche'),
)

SEMESTRE = (
    (0, 'I'),
    (1, 'II'),
)

SECCION = (
    ('Aula', (
            (0, 'A'),
            (1, 'B'),
            (2, 'C'),
            (3, 'D'),
            (4, 'E'),
            (5, 'F'),
            (6, 'G'),
        )
    ),
    ('Laboratorio', (
            (7, 'LAB. 1'),
            (8, 'LAB. 2'),
            (9, 'LAB. 3'),
        )
    ),
)

class Campus(models.Model):
    ciclo        = models.ForeignKey(Ciclo)
    seccion      = models.IntegerField('Sección', choices=SECCION)
    semestre     = models.IntegerField('Semestre', choices=SEMESTRE)
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_fin    = models.DateField('Fecha de Fin')
    turno        = models.IntegerField('Turno', choices=TURNO)
    precio       = models.ForeignKey(Concepto)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campus"
        unique_together = (('ciclo', 'seccion','semestre','fecha_inicio','fecha_fin','turno','precio'),)

    def __unicode__(self):
        return u'%s - %s' % (self.get_turno(),self.get_seccion())

    def get_turno(self):
        t = ['Manana','Tarde','Noche']
        return u'%s' % t[self.turno]

    def get_seccion(self):
        t = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'LAB. 1', 'LAB. 2', 'LAB. 3',]
        return u'%s' % t[self.seccion]

class AlumnoCampus(models.Model):
    alumno     = models.ForeignKey(Alumno)
    campus     = models.ForeignKey(Campus)
    total      = models.DecimalField('Total', max_digits=8, decimal_places=1)
    deuda      = models.DecimalField('Deuda', max_digits=8, decimal_places=1)
    confirmado = models.BooleanField('¿Confirmado?', default = False)
    actual     = models.BooleanField('Actual', default = True)

    class Meta:
        unique_together = (('alumno', 'campus','total','deuda','confirmado','actual'),)
