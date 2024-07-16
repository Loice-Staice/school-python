from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # description = models.TextField()
    duration = models.IntegerField()
    # credits = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.class_id}"

