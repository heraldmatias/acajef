from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('campus.views',
	url(r'^crear/$','campus', name='campus-registrar'),
	url(r'^listar/$','campus_listar', name='campus-listar'),
	#(r'^registro-academico/$','wvbacademico.views.registro_academico'),
	#(r'^form/campus/$','wvbacademico.views.campus'),
	#(r'^json/boleta-campus/(?P<codigo_alumno>\d+)/$','wvbacademico.views.alumno_boleta_json'),
	#(r'^ajax/historial-academico/(?P<alumno_codigo>\w+)/$','wvbacademico.views.historial_academico_ajax'),
	#(r'^ajax/alumno-campus/(?P<ciclo_id>\d+)-(?P<fecha_inicio>\w+)-(?P<seccion>\w+)-(?P<semestre>\d+)/$','wvbacademico.views.alumnos_matriculados_ajax'),
)
