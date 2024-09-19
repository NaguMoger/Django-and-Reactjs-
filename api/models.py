from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    grade = models.CharField(max_length=2)
    address = models.TextField()
    contect_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.first_name