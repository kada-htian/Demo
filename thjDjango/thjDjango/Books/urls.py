from django.conf.urls.defaults import *

urlpatterns = patterns('thjDjango.Books',
	url(r'^$', 'views.book_index', name='home123'),
	url(r'^test1$', 'views.test1'),
)
