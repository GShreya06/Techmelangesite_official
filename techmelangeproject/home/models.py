from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    collegenm=models.CharField(max_length=122)
    events=models.CharField(max_length=122)

class festdesc(models.Model):
    fest_name=models.CharField(max_length=50)
    fest_desc=models.TextField(max_length=1000)


class sponsers(models.Model):
    spon_name=models.CharField(max_length=50)
    spon_logo=models.FileField(upload_to="pics/", max_length = 250, null = True, default = None)
    

class teachcoor(models.Model):
    teach_name=models.CharField(max_length=50)
    teach_img=models.FileField(upload_to="pics/", max_length = 250, null = True, default = None)
    url=models.URLField(max_length=100000)
    

   
     