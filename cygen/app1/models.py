from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(unique=True,max_length=30)
    empno = models.IntegerField(unique=True)
    email = models.EmailField()
    


class Service(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="cygen_images/")
    Startdate = models.DateField()
    Customers = models.IntegerField()
