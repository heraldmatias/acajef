# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "home/index.html", locals())

def home(request):
    return render(request, "home/home.html", locals())

def entrar(request):
    usuario=User
    if request.session.get('usuario', User):
        try:
            usuario = User.objects.get(username__exact=request.POST["user"])
        except (KeyError, usuario.DoesNotExist):
            return render(request, "wvb/index.html",{"error_message":"Por favor ingrese valores correctos."},)
        else:
            if usuario.is_authenticated() and usuario.check_password(request.POST["pass"]):
                request.session['usuario']=usuario
                return HttpResponseRedirect('/wvb/home')
            else:
                return render(request, "home/index.html",{"error_message":"Por favor ingrese valores correctos."},)
    else:
        return render(request, "home/index.html",{"error_message":"Por favor ingrese valores correctos."},)
