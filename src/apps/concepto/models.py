from django.db import models

class Concepto(models.Model):
    concepto     = models.CharField('Concepto', max_length = 140)
    precio       = models.DecimalField('Precio', max_digits=8, decimal_places=1)

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"

    def __unicode__(self):
        return u'%s' % self.concepto
