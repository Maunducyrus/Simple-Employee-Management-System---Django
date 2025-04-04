from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_contact = models.CharField(max_length=15)