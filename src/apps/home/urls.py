from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('home.views',
    url(r'^$','index', name='wvb'),
	url(r'^home/$','home', name='wvb-home'),
	url(r'^login/$','entrar', name='wvb-login'),
)
