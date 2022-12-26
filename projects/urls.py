from django.urls import path
from . import views


urlpatterns = [
    path('' , views.ProjectListViews.as_view() , name = 'Projects_list'),
    path('project/create' , views.ProjectCreateView.as_view() , name = 'Project_create')
]

