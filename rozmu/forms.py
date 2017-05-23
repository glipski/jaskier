from django import forms

class NewMessage(forms.Form):
    Text=forms.CharField(widget=forms.Textarea(attrs={'id': 'pole'}))
