from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('campus.views',
	url(r'^crear/$','campus', name='campus-registrar'),
	url(r'^listar/$','campus_listar', name='campus-listar'),
	url(r'^nuevo/listar/(?P<campus_id>\d+)/$','campus_new_listar', name='campus-nuevo-listar'),
	url(r'^registrar/$','campus', name='campus-registrar'),
	url(r'^matriculado/(?P<carrera_id>\d+)-(?P<ano>\d+)-(?P<turno>\d+)/json/$','campus_matriculado', name='campus-matriculado-json'),
	url(r'^matriculado/alumnos/(?P<campus_id>\d+)/json/$','campus_matriculado_alumno', name='campus-matriculado-alumno-json'),
	url(r'^registro-academico/$','registro_academico', name='campus-registro-academico'),
	url(r'^registrar/registro-academico/$','registro_academico', name='campus-registrar-registro-academico'),
	url(r'^registro-academico/(?P<ciclo_id>\d+)-(?P<ano>\d+)-(?P<seccion>\d+)-(?P<turno>\d+)-(?P<semestre>\d+)/ajax/$','registro_academico_ajax',name='campus-registro-academico'),
)
