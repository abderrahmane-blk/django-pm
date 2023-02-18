from django.shortcuts import render
from django.urls import reverse_lazy ,reverse
from . import models , forms
from django.views.generic import ListView , CreateView , UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#the projects

class ProjectListViews(LoginRequiredMixin,ListView):
    model = models.Project
    template_name = 'project/list.html'

    #this is for the pagination
    paginate_by = 3 

    #this next func is for the search bar

    def get_queryset(self):
        query_set= super().get_queryset()
        where={}
        q = self.request.GET.get("q" , None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


        



class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Project
    template_name = 'project/create.html'
    form_class = forms.ProjectFormView
    success_url = reverse_lazy('Projects_list')


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Project
    template_name = 'project/update.html'
    form_class = forms.ProjectUpdateFormView

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.id])



class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Project
    template_name='project/delete.html'
    success_url =  reverse_lazy('Projects_list')


#now the tasks


class ProjectTaskView(LoginRequiredMixin,CreateView):
    model = models.Task
    fields =['project_id' , 'desc']
    
    http_method_names=['post']

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])


class ProjectTaskEditView(LoginRequiredMixin,UpdateView):
    model = models.Task
    fields =['is_completed']
    
    http_method_names=['post']

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])


class ProjectTaskDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Task

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])