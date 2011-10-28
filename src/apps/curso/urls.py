from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('curso.views',
	url(r'^listar/$','curso', name='curso-listar'),
	url(r'^registrar/$','curso', name='curso-registrar'),
	url(r'^(?P<ciclo_id>\d+)/ajax/$','curso_ajax', name='curso-ajax'),
)
