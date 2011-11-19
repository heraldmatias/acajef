from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('print.views',
	url(r'^lista/asistencia/(?P<campus_id>\d+)/$','campus_lista_asistencia', name='campus-lista-asistencia'),
)
