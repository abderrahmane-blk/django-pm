from django import forms
from . import models

bootstrap_attrs={'class' :'form-control'}

class ProjectFormView(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title' , 'desc' , 'category' ]
        widgets = { 'title': forms.TextInput(attrs=bootstrap_attrs) , 
            'desc' : forms.Textarea(attrs=bootstrap_attrs),
            'category': forms.Select(attrs=bootstrap_attrs), 
        }

class ProjectUpdateFormView(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title' , 'desc' , 'category'  ,'status']
        widgets = { 'title': forms.TextInput(attrs=bootstrap_attrs) , 
            'desc' : forms.Textarea(attrs=bootstrap_attrs),
            'category': forms.Select(attrs=bootstrap_attrs), 
            'status' :forms.Select(attrs=bootstrap_attrs)
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