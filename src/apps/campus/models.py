# -*- coding: utf-8 -*-
from django.db import models
from institucion.models import Ciclo
from alumno.models import Alumno
from pago.models import Monto

"""
App for Campus
"""

TIPO_TURNO = (
    ('1', 'Mañana'),
    ('2', 'Tarde'),
    ('3', 'Noche'),
)

SEMESTRE = (
    (1, 'I'),
    (2, 'II'),
)

SECCION = (
    ('Aula', (
            (1, 'A'),
            (2, 'B'),
            (3, 'C'),
            (4, 'D'),
            (5, 'E'),
            (6, 'F'),
            (7, 'G'),
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
    turno        = models.CharField('Turno',max_length=2, choices=TIPO_TURNO)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campus"

    def __unicode__(self):
        return u'%s - %s' % (self.turno,self.seccion)

class AlumnosCampus(models.Model):
    alumno     = models.ForeignKey(Alumno)
    campus     = models.ForeignKey(Campus)
    monto      = models.ForeignKey(Monto)
    confirmado = models.BooleanField('¿Confirmado?', default = False)
