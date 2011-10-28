# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import AlumnoForm

@login_required(login_url='/wvb/')
def alumno(request):
    alumno_form = AlumnoForm()
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, request.FILES)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect('alumno')
    return render(request,
                    'alumno/alumno.html', 
                    { 'alumno_form': alumno_form })
