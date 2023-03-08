from django.shortcuts import render
from django.urls import reverse_lazy ,reverse
from . import models , forms
from django.views.generic import ListView , CreateView , UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.

#the projects

class ProjectListViews(LoginRequiredMixin,ListView):
    model = models.Project
    template_name = 'project/list.html'

    #this is for the pagination
    paginate_by = 6

    #this next func is for the search bar

    def get_queryset(self):
        query_set= super().get_queryset()
        where={'user_id':self.request.user}
        q = self.request.GET.get("q" , None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


        



class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Project
    template_name = 'project/create.html'
    form_class = forms.ProjectFormView
    success_url = reverse_lazy('Projects_list')

    def form_valid(self, form) :
        form.instance.user=self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = models.Project
    template_name = 'project/update.html'
    form_class = forms.ProjectUpdateFormView

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.id])
    
    



class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Project
    template_name='project/delete.html'
    success_url =  reverse_lazy('Projects_list')

    def test_func(self):
        return self.get_object().user == self.request.user

#now the tasks


class ProjectTaskView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = models.Task
    fields =['project_id' , 'desc']
    
    http_method_names=['post']

    def test_func(self):
        return self.get_object().project_id.user.id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])


class ProjectTaskEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Task
    fields =['is_completed']
    
    http_method_names=['post']

    def test_func(self):
        return self.get_object().project_id.user.id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])


class ProjectTaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Task

    def test_func(self):
        the_proj = self.request.POST.get('project_id','')
        return models.Project.objects.get(pk=the_proj).user.id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse('Project_update' ,args=[self.object.project_id.id])