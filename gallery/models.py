from django.db import models
from sorl.thumbnail import ImageField
class Post(models.Model):
    uploadername = models.CharField(max_length=250)
    picname = models.CharField(max_length=250)
    image = ImageField()
    details = models.TextField()
