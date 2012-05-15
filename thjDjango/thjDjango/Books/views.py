# Create your views here.
import datetime
from django.shortcuts import render_to_response
from thjDjango.Books.models import Book
from django.template.context import Context
from django.template import context
from django.utils.translation import ugettext_lazy


def book_index(request):
	context['output'] = 'ugettext_lazy("Welcome to my site.")'
	return render_to_response('books/index.html',context)


def test1(request):
	print request.LANGUAGE_CODE
	csv_data = (
		('First row', 'Foo', 'Bar', 'Baz'),
		('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
	)

	c = Context({
	'data': csv_data,
	'output': ugettext_lazy("Welcome to my site."),
	})
	return render_to_response('my_template_name.txt',c)
