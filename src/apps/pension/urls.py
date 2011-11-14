from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pension.views',
	url(r'^anular/$','anular',name='pago-anular'),
	url(r'^pension/$','pago_pension',name='pago-pension'),
	url(r'^subsanacion/$','pago_subsanacion',name='pago-subsanacion'),
	url(r'^general/$','pago_general',name='pago-general'),
    url(r'^registrar/pension/$','pago_pension',name='pago-registrar-anular'),
	url(r'^registrar/subsanacion/$','pago_subsanacion',name='pago-registrar-subsanacion'),
	url(r'^registrar/general/$','pago_general',name='pago-registrar-genral'),
	#(r'^json/boleta-campus/(?P<codigo_alumno>\d+)/$','wvbacademico.views.alumno_boleta_json'),
	#(r'^json/boleta-general/(?P<codigo_alumno>\d+)/$','wvbacademico.views.general_boleta_json'),
	#(r'^json/nota_boleta_json/(?P<codigo_alumno>\d+)/$','wvbacademico.views.nota_boleta_json'),
)
