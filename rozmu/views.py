from django.shortcuts import render
from .models import Message
from django.http import HttpResponse

def IndexView(request):
	if request.user.is_authenticated:
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
	else:
		return HttpResponseRedirect('/user/login/')
