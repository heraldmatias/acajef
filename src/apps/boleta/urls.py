from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('boleta.views',
	url(r'^boleta-campus/(?P<codigo_alumno>\w+)/json/$','alumno_boleta_json', name='alumno-boleta-json'),
	url(r'^boleta-alumno-campus/json/','alumno_boleta_nombre_json', name='alumno-boleta-nombre-json'),
	url(r'^(?P<boleta_id>\d+)/imprimir/(?P<campus_id>\d+)/$','boleta_imprimir',name='boleta-imprimir'),
	url(r'^(?P<serie>\w+)/(?P<numero>\w+)/json/$', 'boleta_json',name='boleta-json'),
	#url(r'^boleta-alumno-campus/(?P<alumno>.*)/json/','alumno_boleta_nombre_json', name='alumno-boleta-nombre-json'),
	#(r'^pago/$','wvbacademico.views.pago'),
	#(r'^registro-academico/$','wvbacademico.views.registro_academico'),
	#(r'^boletas/$','wvbacademico.views.boletas'),
	#(r'^form/sustitutorio/$','wvbacademico.views.sustitutorio'),
	#(r'^form/pago/$','wvbacademico.views.pago'),
	#(r'^json/boleta-campus/(?P<codigo_alumno>\d+)/$','wvbacademico.views.alumno_boleta_json'),
	#(r'^json/boleta-general/(?P<codigo_alumno>\d+)/$','wvbacademico.views.general_boleta_json'),
	#(r'^json/nota_boleta_json/(?P<codigo_alumno>\d+)/$','wvbacademico.views.nota_boleta_json'),
	#(r'^json/boletas/(?P<fecha_inicio>\w+)-(?P<fecha_fin>\w+)-(?P<hoy>\d+)-(?P<rows>\d+)/$','wvbacademico.views.boletas_json'),
)
