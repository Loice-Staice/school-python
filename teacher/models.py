from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    # salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
