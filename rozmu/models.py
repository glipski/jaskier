from django.db import models
from django.contrib.auth.models import User

#class Czat(models.Model):
#	Date=models.DateTimeField('date published')
	

class Message(models.Model):
	Date=models.DateTimeField('date published')
	Text=models.TextField()
	Author=models.ForeignKey(User)
	#Czat=models.ForeignKey(Czat)
	def __str__(self):
		s=str(self.Author)
		return s 
