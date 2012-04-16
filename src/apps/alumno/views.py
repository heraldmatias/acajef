# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import AlumnoForm

@login_required(login_url='/wvb/')
def alumno(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, request.FILES)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect('/alumno/registrar/')
    alumno_form = AlumnoForm()
    return render(request,
                    'alumno/alumno.html', 
                    { 'alumno_form': alumno_form })

@login_required(login_url='/wvb/')
def alumno_historial(request):
    return render(request,
                    'alumno/alumno_historial.html', {})

@login_required(login_url='/wvb/')
def alumno_historial_ajax(request,alumno,tipo):
    alu = Alumno.objects.get(pk=alumno)
    if int(tipo) == 1:
        alucampus = AlumnoCampus.objects.filter(alumno = alu)
        return render(request, 'alumno/alumno_historial_ajax.html', {'alucampus': alucampus,'academico':True})