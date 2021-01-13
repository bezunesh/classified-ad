from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	description = models.TextField(max_length=200)
	email = models.EmailField(max_length=20, blank=True, null=True)
	phone = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	published_date = models.DateField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		
		
