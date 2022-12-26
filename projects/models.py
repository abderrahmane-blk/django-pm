from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



#this is a helping class
class ProjectStatus(models.IntegerChoices):
    PENDING = 1,'Pending'
    COMPLETED = 2,'Completed'
    POSTPONED = 3,'Postponed'
    CANCELLED = 4,'Cancelled'



class Project(models.Model):

    title = models.CharField(max_length=200)
    desc =models.TextField(default = 'nothing is specified')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True , null=True)
    
    category =models.ForeignKey(Category , models.PROTECT)
    user =models.ForeignKey(AUTH_USER_MODEL , models.CASCADE)
    
    status =models.IntegerField(
        choices = ProjectStatus.choices ,
        default = ProjectStatus.PENDING
        )
    
    def __str__(self) -> str:
        return self.title


class Task(models.Model):

    desc =models.TextField()
    is_completed = models.BooleanField(default=False)
    project_id =models.ForeignKey(Project , models.CASCADE)

    def __str__(self) -> str:
        return self.desc



