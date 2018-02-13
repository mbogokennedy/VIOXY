from django.db import models

# Create your models here.
class profile(models.Model):
    name= models.CharField(max_length=200)
    description=models.TextField(default='description default text')
    def __str__(self):
        return self.name