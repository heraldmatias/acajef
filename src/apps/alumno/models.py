# -*- coding: utf-8 -*-
from django.db import models

"""
App for Alumno
"""
SEXO = (
        ('F','Femenino'),
        ('M','Masculino'),
        )

class Alumno(models.Model):
    codigo           = models.CharField('Código', max_length=10, blank=True, null=True)
    numero_matricula = models.CharField('Número Matricula', max_length=12, blank=True, null=True)
    apellido         = models.CharField('Apellido', max_length=200)
    nombre           = models.CharField('Nombre', max_length=200)
    dni              = models.CharField('D.N.I.', max_length=12, unique=True)
    telefono         = models.CharField('Teléfono', max_length=10, blank=True, null=True)
    sexo             = models.CharField('Sexo', max_length=1, choices = SEXO, blank=True, null=True)
    celular          = models.CharField('Celular', max_length=12, blank=True, null=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', )
    direccion        = models.TextField('Dirección', blank=True, null=True)
    foto             = models.ImageField('Foto', upload_to='alumno/', blank=True, null=True)
    apoderado        = models.CharField('Apoderado', max_length=250)
    email            = models.EmailField('E-Mail')
    matriculado      = models.BooleanField('Matriculado', default=False)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        unique_together = (('apellido', 'nombre','codigo','dni','numero_matricula'),)

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
		return u'%s,  %s' % (self.apellido, self.nombre)
