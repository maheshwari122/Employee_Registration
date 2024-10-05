from django.db import models

# Create your models here.
class MyBaseModel(models.Model):
    id = models.AutoField(primary_key = True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class EmployeeRegistrationForm(MyBaseModel):
    full_name = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    Date_of_birth = models.DateTimeField(auto_created=True)
    marital_status = models.CharField(max_length=255)
    education = models.CharField(max_length=100)
    residence_address= models.CharField(max_length=255)
    present_address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=150)