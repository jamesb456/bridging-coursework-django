from django.db import models

# Create your models here.
class CV(models.Model):
    email = models.EmailField()
    github_profile = models.URLField(default="")
    linkedin_profile = models.URLField(default="")
    personal_statement = models.TextField(default="")
