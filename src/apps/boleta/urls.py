from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('boleta.views',
	url(r'^boleta-campus/(?P<codigo_alumno>\w+)/json/$','alumno_boleta_json', name='alumno-boleta-json'),
	url(r'^boleta-alumno-campus/json/','alumno_boleta_nombre_json', name='alumno-boleta-nombre-json'),
	url(r'^(?P<boleta_id>\d+)/imprimir/$','boleta_imprimir',name='boleta-imprimir'),
	url(r'^(?P<serie>\w+)/(?P<numero>\w+)/json/$', 'boleta_json',name='boleta-json'),
	url(r'^historial/$', 'boleta_historial',name='boleta-historial'),
)
