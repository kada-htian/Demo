from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=255, blank=True)
	author = models.CharField(max_length=64, blank=True)
	price = models.FloatField(blank=True)

	def __unicode__(self):
		return self.name


class MyBook(Book):
	pass
	def __unicode__(self):
		return self.name