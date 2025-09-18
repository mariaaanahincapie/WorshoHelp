<<<<<<< HEAD
from django.db import models

# create your models here

class Movie(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250) 
    image = models.ImageField(upload_to='movie/images/') 
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self): 
=======

from django.db import models
import numpy as np

def get_default_array():
    default_arr = np.random.rand(1536)
    return default_arr.tobytes()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='movie/images/', default='movie/images/default.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    emb = models.BinaryField(default=get_default_array)

    def __str__(self):
>>>>>>> 5e563f7ad2a049408b115afeef87ff6d19ed582f
        return self.title
