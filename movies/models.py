from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Cast(models.Model):
    director = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)

    def __str__(self):
        return self.director

class Category(models.Model):
    movie_type = models.CharField(max_length=255)

class Review(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, null=True)
    # attachment = models.FileField()

    def __str__(self):
        return '{} - Review'.format(self.movie.name)

class Movie(models.Model):
    name = models.CharField("Movie Name", max_length=255, unique=True)
    description = models.TextField(verbose_name="Movie Description")
    likes = models.IntegerField(default=0, null=True)
    rate = models.PositiveIntegerField(default=0)
    Production_date = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    # banner = models.ImageField(upload_to='movie/images')
    casts = models.ManyToManyField("Cast")

    def __str__(self):
        return self.name
