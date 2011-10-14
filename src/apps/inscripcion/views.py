from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Carrera, Ciclo

def carrera(request):
    if request.method == 'POST':
        carrera, created = Carrera.objects.get_or_create(
                            pk = request.POST["idcarrera"],
                            defaults = {
                                        'carrera'  : request.POST["idcarrera"],
                                        'duracion' : request.POST["duracion"],
                                        'tipo'     : request.POST["tipo"],
                                        'monto'    : request.POST["monto"],
                                        'valido'   : request.POST["valido"],
                                        }
                            )
        carrera.save()
        return HttpResponseRedirect('/wvb/carrera')
	carrera_form = CarreraForm()
	carreras = Carrera.objects.all().order_by('carrera')
	return render(request, 'inscripcion/carrera.html', 
	                {
                        'carrera_form' : carrera_form ,
                        'carreras'     :carreras,
                    },
                 )
