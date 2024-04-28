from django.db import models
from department.models import Department
# Create your models here.
class Doctor (models.Model):
    name= models.CharField(max_length=20)
    description = models.TextField(max_length=100,blank=True, null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    icon_url = models.URLField(max_length=300,blank=True, null=True)
    def __str__(self):
        return self.name
    
