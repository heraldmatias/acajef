# -*- coding: utf-8 -*-
from django.db import models
from campus.models import AlumnoCampus
from concepto.models import Concepto

class Boleta(models.Model):
    alumno        = models.ForeignKey(AlumnoCampus)
    serie         = models.CharField('Serie', max_length=3)
    numero        = models.CharField('Número', max_length=7)
    concepto      = models.ForeignKey(Concepto)
    fecha_emision = models.DateTimeField('Fecha de emisión')
    valido        = models.BooleanField('¿Valida?', default=True)
    importe       = models.DecimalField('Importe', max_digits=8,decimal_places=1)
    saldo         = models.DecimalField('saldo', max_digits=8,decimal_places=1)
    observacion   = models.TextField('Observación', blank=True,null=True)

    class Meta:
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
        unique_together = (('serie', 'numero'),)

    def __unicode__(self):
        return u'%s - %s' % (self.serie,self.numero)

    def get_url_imprimir(self):
        return u'/%s/%s/%s' % ('boleta',self.id,'imprimir')
