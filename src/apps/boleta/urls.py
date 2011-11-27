from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('boleta.views',
	url(r'^boleta-campus/(?P<codigo_alumno>\w+)/json/$','alumno_boleta_json', name='alumno-boleta-json'),
	url(r'^boleta-alumno-campus/json/','alumno_boleta_nombre_json', name='alumno-boleta-nombre-json'),
	url(r'^(?P<boleta_id>\d+)/imprimir/$','boleta_imprimir',name='boleta-imprimir'),
	url(r'^(?P<serie>\w+)/(?P<numero>\w+)/json/$', 'boleta_json',name='boleta-json'),
	url(r'^historial/$', 'boleta_historial',name='boleta-historial'),
	url(r'^boleta-alumno-campus-id/json/','alumno_boleta_id_json', name='alumno-boleta-id-json'),
	url(r'^buscar/(?P<serie>\w+)/(?P<numero>\w+)/(?P<alumno>\w+)/(?P<fecha_inicio>\w+)/(?P<fecha_fin>\w+)/(?P<anulado>\w+)/json/','boleta_buscar', name='boleta-buscar'),
)
