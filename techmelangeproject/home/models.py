from django.db import models

# Create your models here.

# Shalini Added 
class festdesc(models.Model):
    fest_name=models.CharField(max_length=2000)
    fest_desc=models.TextField(max_length=5000)


class sponsers(models.Model):
    spon_name=models.CharField(max_length=50)
    spon_logo=models.FileField(upload_to="static/", max_length = 250, null = True, default = None)
    

class teachcoor(models.Model):
    teach_name=models.CharField(max_length=50)
    teach_img=models.FileField(upload_to="static/", max_length = 250, null = True, default = None)
    url=models.URLField(max_length=100000)
 
# Nishu Added
class studcoor(models.Model):
    s_name=models.CharField(max_length=122)
    s_desc=models.TextField()
    s_image=models.FileField(upload_to="static/",max_length=250,null=True,default=None)
    s_link=models.URLField()

# Shreya Added 
class events(models.Model):
    e_name=models.CharField(max_length=50)
    e_desc=models.CharField(max_length=1000)
    e_img=models.ImageField()
    e_frm=models.URLField(max_length=200,null=True)
    
class contacts(models.Model):
    C_email=models.CharField(max_length=50)
    C_mobile=models.CharField(max_length=10,null=True)

class main(models.Model):
    mname=models.CharField(max_length=50)
    mdesc=models.TextField(max_length=1000)
    mdate=models.CharField(max_length=50)
    mbg=models.ImageField()
   

#for commit
