from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    collegenm=models.CharField(max_length=122)
    events=models.CharField(max_length=122)

class festdesc(models.Model):
    fest_name=models.CharField(max_length=50)
<<<<<<< HEAD
    fest_desc=models.TextField(max_length=1000)


class sponsers(models.Model):
    spon_name=models.CharField(max_length=50)
    spon_logo=models.FileField(upload_to="pics/", max_length = 250, null = True, default = None)
=======
    fest_desc=models.CharField(max_length=100)
    fest_bg=models.ImageField(null=True)
    
class events(models.Model):
    e_name=models.CharField(max_length=50)
    e_desc=models.CharField(max_length=100)
    e_img=models.ImageField()
    e_frm=models.URLField(max_length=200,null=True)
>>>>>>> 2f92d2b76ed3506dc36c32c465d91f92bbe09d05
    

class teachcoor(models.Model):
    teach_name=models.CharField(max_length=50)
    teach_img=models.FileField(upload_to="pics/", max_length = 250, null = True, default = None)
    url=models.URLField(max_length=100000)
    

   
     