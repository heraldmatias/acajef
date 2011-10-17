# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "home/index.html", locals())

@login_required(login_url='/wvb/')
def home(request):
    return render(request, "home/home.html", locals())

def entrar(request):
    username = request.POST['user']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/wvb/home/')
    else:
        return render(request,
                        "home/index.html",
                        {"error_message":"Por favor ingrese valores correctos."})

@login_required(login_url='/wvb/')
def salir(request):
    logout(request)
    return redirect('/wvb/')

@login_required(login_url='/wvb/')
def academico(request):
    return render(request, "home/academico.html")

@login_required(login_url='/wvb/')
def pago(request):
    return render(request, "home/pago.html")

