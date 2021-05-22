from django.db import models

# Create your models here.

class photo(models.Model):
    image_upload = models.ImageField(upload_to='images/')  #the image will upload to ~/media/images.
    video_upload = models.FileField(upload_to='images/')  #the image will upload to ~/media/images.
