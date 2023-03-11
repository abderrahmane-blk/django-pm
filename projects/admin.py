from django.contrib import admin
from . import models
from django.db.models import Count

# Register your models here.

#admin.site.register(models.Category)
#admin.site.register(models.Project)
#admin.site.register(models.Task)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display =['title' , 'user' , 'category'  ,'updated_at' ,'status' ,'tasks_count']
    list_per_page = 10
    list_select_related =['user' ,'category']

    def tasks_count(self , obj):
        return obj.yyyy

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset =queryset.annotate( yyyy = Count('task'))
        return queryset

    list_editable =['status']


@admin.register(models.Task)
class ProjectAdmin(admin.ModelAdmin):
    list_display =['id' , 'project_id' , 'is_completed']
    list_per_page = 10
    list_editable =['is_completed']

