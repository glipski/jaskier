from django.shortcuts import render
from .models import Message
from django.http import HttpResponse

def IndexView(request):
	s = ""
	lista = Message.objects.all()
	for message in lista:
		s+="<b>"
		s+=str(message.Author)
		s+="</b>"
		s+="<br>"
		s+=str(message.Text)
		s+="<br>"
	return HttpResponse(s)
