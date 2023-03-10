from django import forms
from . import models
from django.utils.translation import gettext as _

bootstrap_attrs={'class' :'form-control'}

class ProjectFormView(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title' , 'desc' , 'category' ]
        labels ={
            'title' :_('title') ,
            'desc' :_('desc') ,
            'category':_('category') 

        }
        widgets = { 'title': forms.TextInput(attrs=bootstrap_attrs) , 
            'desc' : forms.Textarea(attrs=bootstrap_attrs),
            'category': forms.Select(attrs=bootstrap_attrs), 
        }

class ProjectUpdateFormView(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title' , 'desc' , 'category'  ,'status']
        labels ={
            'title' :_('title') ,
            'desc' :_('desc') ,
            'category':_('category') ,  
            'status':_('status') 

        }
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