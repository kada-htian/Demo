from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('DjangoDemo.MyTest.views',
	url(r'current_datetime/$', 'current_datetime'),
)
