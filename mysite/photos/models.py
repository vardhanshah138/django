from django.db import models

# Create your models here.

class photo(models.Model):
    title = models.CharField(max_length=50)
    record = models.FileField(upload_to='images/')  #the image will upload to ~/media/images.
