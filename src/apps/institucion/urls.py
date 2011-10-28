from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('institucion.views',
	url(r'^carrera/$','carrera', name='institucion-carrera'),
	url(r'^carrera/registrar/$','carrera', name='institucion-carrera-registrar'),
	url(r'^carrera/(?P<carrera_id>\d+)/json/$','carrera_json', name='institucion-carrera-json'),
	url(r'^ciclos/(?P<carrera_id>\d+)/json/$','cilos_json', name='institucion-ciclo-json'),
)
