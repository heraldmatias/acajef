from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from campus.models import AlumnoCampus
from alumno.models import Alumno
from models import Nota

@login_required(login_url='/wvb/')
def get_curso_desaprobado(request, alumno_codigo):
    alumno_campus = AlumnoCampus.objects.filter(alumno = Alumno.objects.get(codigo = alumno_codigo))
    cursos_desaprovados = Nota.objects.filter(alumno_campus__in = alumno_campus)
    json_serializer = serializers.get_serializer("json")()
    resultado = json_serializer.serialize(cursos_desaprovados, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')
    #return HttpResponse(simplejson.dumps(cursos_desaprovados),mimetype='application/json')
