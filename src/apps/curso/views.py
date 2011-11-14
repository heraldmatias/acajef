from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Curso
from forms import CursoForm
from institucion.forms import CicloForm
from institucion.models import Carrera, Ciclo
from docente.models import Docente

@login_required(login_url='/wvb/')
def curso(request):
    ciclo_form = CicloForm()
    if request.method == 'POST':
        ciclo = Ciclo.objects.get(pk=request.POST['ciclo'])
        curso = Curso.objects.create(curso=request.POST['curso'],ciclo=ciclo)
        curso.save()
        return redirect('/curso/listar/')
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('pk')
    cursos = ciclos[0].curso_set.all().order_by('-pk')
    return render(request, 'curso/curso.html', { 'ciclo_form':ciclo_form, "carrera":carrera, 'ciclos':ciclos, 'cursos':cursos},)

@login_required(login_url='/wvb/')
def curso_ajax(request,ciclo_id):
    cursos = Ciclo.objects.get(pk=ciclo_id).curso_set.all().order_by("curso")
    return render(request, 'curso/curso_ajax.html', { 'cursos': cursos})

@login_required(login_url='/wvb/')
def curso_campus_ajax(request,ciclo_id):
	ciclo = Ciclo.objects.get(pk=ciclo_id)
	docentes = Docente.objects.filter(activo=True)
	return render(request, 'curso/curso_campus_ajax.html', { 'ciclo': ciclo,'docentes':docentes})
