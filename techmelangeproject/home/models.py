from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    collegenm=models.CharField(max_length=122)
    events=models.CharField(max_length=122)
