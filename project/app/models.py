from operator import mod
from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    desc = models.TextField(blank=True,null=True)
    schoolname = models.CharField(max_length=200,blank=True,null=True)
    subjectname = models.CharField(max_length=200,blank=True,null=True)
    skills = models.CharField(max_length=200,blank=True,null=True)
    project = models.CharField(max_length=200,blank=True,null=True)

