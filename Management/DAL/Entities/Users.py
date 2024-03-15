from django.db import models

class Users(models.Model):
    UserID=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=20,unique=True)
    firstname=models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50, null=False)
    Password=models.CharField(max_length=16)

