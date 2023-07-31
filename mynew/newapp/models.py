from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=20)
    Address = models.TextField()
    Phone = models.CharField(max_length=10)
    def __str__(self):
        return self.Name

