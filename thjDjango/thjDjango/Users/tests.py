"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from thjDjango.Users.models import Provide


class UsersTest(TestCase):
	def test_add(self):
		user = Provide()
		user.first_name = 'tt'
		user.last_name = 'ss'
		user.provider_name = 'pp_tt_ss'
		user.save()
	def test_get(self):
		users = Provide.objects.all()
		for user in users:
			print user.id

