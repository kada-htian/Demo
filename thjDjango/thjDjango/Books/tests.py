"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from thjDjango.Books.models import Book

def my_func(a_list, idx):
	return a_list[idx]

class SimpleTest(TestCase):
	def setUp(self):
		self.a = ['larry', 'curly', 'moe']
	def test01(self):		
		self.assertEqual(my_func(self.a, 0), 'larry')
		self.assertEqual(my_func(self.a, 1), 'curly')
	def test_book_delete(self):
		Book.objects.all().delete()

class BooksTest(TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_book_add(self):
		book = Book()	
		book.name = 'test'
		book.author = 'thj'
		book.price = 123.4
		book.save()
		
	def test_book_delete(self):
		Book.objects.all().delete()

