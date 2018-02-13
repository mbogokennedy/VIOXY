from django.db import models
from django.utils import timezone


class additem(models.Model):
     business_name = models.CharField(max_length=100, blank=False, null=False)
     description = models.TextField(default='write a description text')
     email = models.EmailField(help_text='email@example.com')
     contact = models.CharField(max_length=100, help_text='070000000')
     date_added = models.DateField(default=timezone.now)
     def __str__ (self):
         
         return('<Name: {}, Date: {}>'.format(self.business_name, self.date_added))


 #  image = models.ImageField(width_field=None, height_field=None) pip install pillow