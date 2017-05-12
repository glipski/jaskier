from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate

def IndexView(request):
	s = "Zalogowany jako "
	s+=str(request.user.username)
	s+="<br>"
	s+='<a href="/user/logout">Wyloguj się </a> <br>'
	lista = Message.objects.all()
	for message in lista:
		s+="<b>"
		s+=str(message.Author)
		s+="</b>"
		s+="<br>"
		s+=str(message.Text)
		s+="<br>"
	return HttpResponse(s)

def authentic(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/user/login")
	return IndexView(request) 
	

