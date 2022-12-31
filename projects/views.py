from django.shortcuts import render
from django.urls import reverse_lazy ,reverse
from . import models , forms
from django.views.generic import ListView , CreateView , UpdateView ,DeleteView
# Create your views here.

#the projects

class ProjectListViews(ListView):
    model = models.Project
    template_name = 'project/list.html'

class ProjectCreateView(CreateView):
    model = models.Project
    template_name = 'project/create.html'
    form_class = forms.ProjectFormView
    success_url = reverse_lazy('Projects_list')


class ProjectUpdateView(UpdateView):
    model = models.Project
    template_name = 'project/update.html'
    form_class = forms.ProjectUpdateFormView

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.id])



class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name='project/delete.html'
    success_url =  reverse_lazy('Projects_list')


#now the tasks


class ProjectTaskView(CreateView):
    model = models.Task
    fields =['project_id' , 'desc']
    
    http_method_names=['post']

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])


class ProjectTaskEditView(UpdateView):
    model = models.Task
    fields =['is_completed']
    
    http_method_names=['post']

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])


class ProjectTaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])