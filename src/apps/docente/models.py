# -*- coding: utf-8 -*-
from django.db import models

"""
App for Docente
"""
class Docente(models.Model):
    nombre     = models.CharField('Nombre', max_length=150)
    apellido   = models.CharField('Apellido', max_length=150)
    dni        = models.CharField('D.N.I.', max_length=8, unique=True)
    fijo       = models.CharField('Fijo', max_length=10,blank=True,null=True)
    celular    = models.CharField('Celular', max_length=12,blank=True,null=True)
    direccion  = models.TextField('Dirección', blank=True,null=True)
    email      = models.EmailField('E-mail', blank=True, null=True)
    activo     = models.BooleanField('Activo', default=False)
    curriculum = models.FileField('Curriculum', upload_to='curriculum',blank=True,null=True)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        unique_together = (('apellido', 'nombre'),)

    def __unicode__(self):
        return u'%s, %s' % (self.apellido,self.nombre)
