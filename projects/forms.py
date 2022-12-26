from django import forms
from . import models

class ProjectFormView(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title' , 'desc' , 'category' ]
        widgets = { 'title': forms.TextInput() , 
            'desc' : forms.Textarea(),
            'category': forms.Select(), 
        }