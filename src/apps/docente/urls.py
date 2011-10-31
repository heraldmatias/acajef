from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('docente.views',
	url(r'^listar/$','docente', name='docente-listar'),
	url(r'^registrar/$','docente', name='docente-registar'),
	url(r'^(?P<docente_id>\d+)/json/$','docente_json', name='docente-json'),
)
