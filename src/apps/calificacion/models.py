from django.db import models
from curso.models import CursoDocente
from boleta.models import Boleta
from campus.models import AlumnosCampus

class Nota(models.Model):
    curso_docente  = models.ForeignKey(CursoDocente)
    alumno_campus  = models.ForeignKey(AlumnosCampus)
    nota           = models.IntegerField('Nota')

    def __unicode__(self):
        return u'%s' % self.nota

class Recuperacion(models.Model):
    nota     = models.ForeignKey(Nota)
    boleta   = models.ForeignKey(Boleta)
    new_nota = models.IntegerField('Nueva nota', default=0)
    old_nota = models.IntegerField('Vieja nota', default=0)
