from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewMessage
from django.utils import timezone

def IndexView(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect('/user/login/')

	lista = Message.objects.all()
	if request.method=="POST":
		form=NewMessage(request.POST)
		if form.is_valid():
			t=form.cleaned_data['Text']
			m=Message(Text=t,Author=request.user,Date=timezone.now())
			m.save()
	else:
		form=NewMessage()		
	return render(request,'rozmu/czat.html',{'form':form,'lista':lista})
