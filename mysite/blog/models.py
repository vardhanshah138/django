from django.db import models

# Create your models here.
class Blog(models.Model):
    media_name = models.CharField(max_length=50)
    media_img_video = models.FileField(null=True,blank=True,upload_to='images/')