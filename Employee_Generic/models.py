from django.db import models

# Create your models here.
class Employee_generic(models.Model):
    emp_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)

    def __str__(self):
        return self.name



