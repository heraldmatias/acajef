from django.db import models
from institucion.models import Ciclo
from docente.models import Docente
from campus.models import Campus

"""
App for Curso
"""

class Curso(models.Model):
    ciclo = models.ForeignKey(Ciclo)
    curso = models.CharField('Curso', max_length=30)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __unicode__(self):
        return u'%s' % (self.curso)

class CursoDocente(models.Model):
    docente = models.ForeignKey(Docente)
    curso   = models.ForeignKey(Curso)
    campus  = models.ForeignKey(Campus)
