from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs= {'placeholder':'Task title...'}),  label=False)

    due = forms.DateTimeField(widget= forms.DateInput(attrs={'placeholder':'Due date...'}),label= False)

    class Meta:
        model = Task
        fields = ['title', 'due']


class UpdateForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))
    due = forms.DateTimeField(widget= forms.DateInput(attrs={ 'placeholder':'Due date...'}),label= False)

    class Meta:
        model = Task
        fields = ['title', 'due', 'complete']
