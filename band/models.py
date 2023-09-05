from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    bio = models.TextField()
    members = models.ManyToManyField(User, related_name='bands')

    def __str__(self):
        return self.name

class Song(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

