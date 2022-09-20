from django.db import models

# Create your models here.
class Student(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Gender = models.CharField(max_length=7)
    Date_of_Birth = models.DateField()
    Mobile_Number = models.BigIntegerField()
    E_Mail = models.EmailField()
    Adm_Num_and_Date = models.CharField(max_length=60)
    deptmt = models.CharField(max_length=255)
    Father_name = models.CharField(max_length=40)
    Mother_name = models.CharField(max_length=40)
    Father_mob = models.BigIntegerField()
    Mother_mob = models.BigIntegerField()
    Address = models.CharField(max_length=300)
    User_Photo = models.ImageField(upload_to = 'image/', null=True)