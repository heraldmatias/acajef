# -*- coding: utf-8 -*-
from django.db import models
from boleta.models import Boleta
from campus.models import AlumnoCampus

"""
App for Pago
"""

class Pension(models.Model):
    alumno_campus = models.ForeignKey(AlumnoCampus)
    boleta        = models.ForeignKey(Boleta)
