from xhtml2pdf import pisa
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import timedelta
from campus.models import AlumnoCampus, Campus
import cgi
import cStringIO as StringIO

def print_pdf(html):
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

@login_required(login_url='/wvb/')
def campus_lista_asistencia(request, campus_id):
    nombre_dia = ['Lun','Mar','Mie','Jue','Vie']
    campus = Campus.objects.get(pk = campus_id)
    alumnos = AlumnoCampus.objects.filter(campus = campus)
    fecha_inicio = campus.fecha_inicio
    fecha_fin = campus.fecha_fin
    semanas = fecha_fin - fecha_inicio 
    dias = []
    asistencia = []
    for d in range(0,(semanas.days+1)):
        fecha = fecha_inicio + timedelta(days = d)
        if not (fecha.weekday()==5 or  fecha.weekday()==6):
            dias.append((nombre_dia[fecha.weekday()],fecha.day))
        if len(dias) == 10:
            asistencia.append(dias)
            dias = []
    if len(dias) > 0:
        asistencia.append(dias)
    pdf_html_lista = render_to_string('print/campus-lista-asistencia.html',
                         { 'campus' : campus, "alumnos" : alumnos, 'asistencia' : asistencia,},
                         context_instance=RequestContext(request))
    return print_pdf(pdf_html_lista)

@login_required(login_url='/wvb/')
def boletas_for_dates(request, campus_id):
    nombre_dia = ['Lun','Mar','Mie','Jue','Vie']
