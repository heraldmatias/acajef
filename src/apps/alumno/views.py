# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import AlumnoForm

def alumno(request):
    alumno_form = AlumnoForm()
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST,request.FILES)
        if alumno_form.is_valid():
            alumno_form.save()
            #picture_uploaded(request.FILES["foto"])
            return HttpResponseRedirect('/wvb/alumno')
    return render(request,'alumno/alumno.html', { 'alumno_form': alumno_form },)
