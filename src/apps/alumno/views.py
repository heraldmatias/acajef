# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from forms import AlumnoForm

def alumno(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, request.FILES)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect('alumno')
    alumno_form = AlumnoForm()
    return render(request,
                    'alumno/alumno.html', 
                    { 'alumno_form': alumno_form })
