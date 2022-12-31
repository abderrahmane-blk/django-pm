from django.urls import path
from . import views


urlpatterns = [
    path('' , views.ProjectListViews.as_view() , name = 'Projects_list'),
    path('project/create' , views.ProjectCreateView.as_view() , name = 'Project_create'),
    path('project/update/<int:pk>' , views.ProjectUpdateView.as_view() , name = 'Project_update'),
    path('project/delete/<int:pk>' , views.ProjectDeleteView.as_view() , name = 'Project_delete'),
    path('task/create/' , views.ProjectTaskView.as_view() , name = 'task_create'),
    path('task/edit/<int:pk>' , views.ProjectTaskEditView.as_view() , name = 'task_update'),
    path('task/delete/<int:pk>' , views.ProjectTaskDeleteView.as_view() , name = 'task_delete')



]

