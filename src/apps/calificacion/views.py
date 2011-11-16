from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson
from django.db.models import Q
from campus.models import AlumnoCampus
from alumno.models import Alumno
from models import Nota

@login_required(login_url='/wvb/')
def get_curso_desaprobado(request, alumno_codigo):
    alumno_campus = AlumnoCampus.objects.filter(alumno = Alumno.objects.get(codigo = alumno_codigo))
    cursos_desaprovados = [{'id' : nota.pk, 'curso': nota.curso_docente.curso.curso} for nota in Nota.objects.filter(Q(alumno_campus__in = alumno_campus), Q(nota__lte=10))]
    return HttpResponse(simplejson.dumps(cursos_desaprovados),mimetype='application/json')
