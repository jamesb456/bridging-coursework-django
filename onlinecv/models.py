from django.db import models
from datetime import date
# Create your models here.
class CV(models.Model):
    email = models.EmailField()
    github_profile = models.URLField(default="")
    linkedin_profile = models.URLField(default="")
    personal_statement = models.TextField(default="")

class Qualification(models.Model):
    linked_cv = models.ForeignKey(CV,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default="")
    start_date = models.DateField(default=date(1970,1,1))
    end_date = models.DateField(default=date(1970,1,2))
    description = models.TextField(default="")