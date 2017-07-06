# -*- coding: utf-8 -*-


from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder':' login'}),
	)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder':' hasło'}),
	)


