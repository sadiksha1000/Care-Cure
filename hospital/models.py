from django.db import models
from django.contrib import messages
from django.core import validators
from django.core.validators import *

class Service(models.Model):
    name=models.CharField(max_length=300,null=True)
    description=models.CharField(max_length=200,null=True,validators=[validators.MinLengthValidator(50)])
    image = models.ImageField(upload_to='static/uploads')
    treatment_name=models.CharField(max_length=300,null=True)
    treatment_description=models.CharField(max_length=2000,null=True,validators=[validators.MinLengthValidator(50)])

    def __str__(self):
        return self.name

    # @property
    # def imageURL(self):
    #     try:
    #         url=self.image.url
    #     except:
    #         url=""
    #     return url

class Doctor(models.Model):
    doctor_name=models.CharField(max_length=300, null=True,name="Name")
    doctor_designation=models.CharField(max_length=300,null=True, name="Designation")
    doctor_email=models.CharField(max_length=1000,null=True,name="Email")
    doctor_image=models.ImageField(upload_to='static/uploads',name="Image",null=True,blank=True)
    doctor_schedule=models.CharField(max_length=200, null=True,name="Schedule")
    work_experience=models.CharField(max_length=5000,null=True,name="Experience")
    doctor_background=models.CharField(max_length=5000,null=True,name="Background")



