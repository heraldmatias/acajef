from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pago.views',
	url(r'^anular/$','anular',name='pago-anular'),
	url(r'^pension/$','pago_pension',name='pago-pension'),
	url(r'^subsanacion/$','pago_subsanacion',name='pago-subsanacion'),
	url(r'^general/$','pago_general',name='pago-general'),
    url(r'^registrar/pension/$','pago_pension',name='pago-registrar-anular'),
	url(r'^registrar/subsanacion/$','pago_subsanacion',name='pago-registrar-subsanacion'),
	url(r'^registrar/general/$','pago_general',name='pago-registrar-genral'),
	url(r'^registrar/pago-subsanar/$','pago_subsanacion',name='registrar-pago-subsanar'),
)
