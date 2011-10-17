from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('home.views',
    url(r'^$','index', name='wvb'),
	url(r'^home/$','home', name='wvb-home'),
	url(r'^login/$','entrar', name='wvb-login'),
	url(r'^logout/$','salir', name='wvb-salir'),
	url(r'^academico/$','academico', name='wvb-academico'),
	url(r'^pago/$','pago', name='wvb-pago'),
)
