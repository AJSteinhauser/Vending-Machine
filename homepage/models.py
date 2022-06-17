from django.db import models

# Create your models here.

class Users(models.Model):
    userID = models.AutoField(primary_key=True);
    username = models.CharField(max_length=255,blank=True,null=True);
    userPassword = models.CharField(max_length=255,blank=True,null=True);
    userCash = models.DecimalField(default=100.00,max_digits=5,decimal_places=2);