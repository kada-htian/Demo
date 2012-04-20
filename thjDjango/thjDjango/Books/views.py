# Create your views here.
import datetime
from django.shortcuts import render_to_response
from thjDjango.Books.models import Book

def book_index(request):
	now = datetime.datetime.now()
	hello_world = 'hello world'
	return render_to_response('books/index.html',locals())
	book = Book()
	book.author = "me"
	
