from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate

def IndexView(request):
	if request.user.is_authenticated:
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
	else:
		return HttpResponseRedirect('/user/login/')

def authentic(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/user/login")
	return IndexView(request) 
	


