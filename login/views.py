from django.shortcuts import render
from login.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

# Create your views here.

def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(request, username=u, password=p)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/czat/')
			else:
				return HttpResponseRedirect('/nie/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

def registration_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = User.objects.create_user(username=u, password=p)
			user.save()
			login(request, user)
			return HttpResponseRedirect('/czat/')
	else:
		form = LoginForm()
	return render(request, 'registration.html', {'form': form})
