from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('alumno.views',
    url(r'^guardar/$', 'alumno', name='alumno-listar'),
    url(r'^registrar/$','alumno', name='alumno-registrar'),
    url(r'^historial/$','alumno_historial', name='alumno-historial'),
    url(r'^historial/(?P<alumno>\d+)-(?P<tipo>\d+)/ajax/$','alumno_historial_ajax', name='alumno-historial-ajax'),
)
