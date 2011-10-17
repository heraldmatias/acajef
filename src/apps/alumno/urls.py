from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('alumno.views',
    url(r'^listar/$', 'alumno', name='alumno-listar'),
    url(r'^registrar/$','alumno', name='alumno-registrar'),
)
