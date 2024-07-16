from django.db import models

# Create your models here.
class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    section = models.CharField(max_length=10)
    # start_date = models.DateField()
    # end_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} {self.id}"