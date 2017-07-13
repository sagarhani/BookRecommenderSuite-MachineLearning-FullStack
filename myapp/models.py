from __future__ import unicode_literals

from django.db import models

# Create your models here.

class genre(models.Model):
	gid=models.IntegerField()
	gname=models.CharField(max_length=30)

	def __str__(self):
		return self.gname

class book(models.Model):
	name = models.CharField(max_length=100)
	isbn = models.CharField(max_length=15)
	author = models.CharField(max_length=120)
	year = models.CharField(max_length=15)
	genre_name = models.IntegerField()
	rating = models.IntegerField()
	description = models.CharField(max_length=2000)
	img = models.ImageField()

	def __str__(self):
		return self.name

class reviews(models.Model):
	name = models.CharField(max_length=150)
	bookid = models.IntegerField()
	review = models.CharField(max_length=750)
	rating = models.IntegerField(default=0)

	def __str__(self):
		return self.name