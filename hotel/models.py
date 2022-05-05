from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hotel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    output_images_list = models.TextField(default='')
