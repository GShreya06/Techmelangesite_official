from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    collegenm=models.CharField(max_length=122)
    events=models.CharField(max_length=122)

class festdesc(models.Model):
    fest_name=models.CharField(max_length=50)
    fest_desc=models.CharField(max_length=100)
    fest_bg=models.ImageField(null=True)
    
class events(models.Model):
    e_name=models.CharField(max_length=50)
    e_desc=models.CharField(max_length=100)
    e_img=models.ImageField()
    e_frm=models.URLField(max_length=200,null=True)
    
     