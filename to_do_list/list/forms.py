from django import forms
from .models import date,task

class dateform(forms.ModelForm):
    class Meta:
        model=date
        fields= ['Date']

class taskform(forms.ModelForm):
    class Meta:
        model=task
        fields=['Date', 'Name', 'Description', 'Note']