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

class ProjectUpdateFormView(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title' , 'desc' , 'category'  ,'status']
        widgets = { 'title': forms.TextInput() , 
            'desc' : forms.Textarea(),
            'category': forms.Select(), 
            'status' :forms.Select()
        }

#useless
'''class ProjectTaskFormView(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['desc']
        widgets = { 'title': forms.TextInput() , 
            'desc' : forms.Textarea(),
            
        }
        '''