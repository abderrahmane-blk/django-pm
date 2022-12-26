from django.shortcuts import render
from django.urls import reverse_lazy
from . import models , forms
from django.views.generic import ListView , CreateView
# Create your views here.



class ProjectListViews(ListView):
    model = models.Project
    template_name = 'project/list.html'

class ProjectCreateView(CreateView):
    model = models.Project
    template_name = 'project/create.html'
    form_class = forms.ProjectFormView
    success_url = reverse_lazy('project_list')

