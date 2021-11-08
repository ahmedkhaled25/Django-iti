from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField("Movie Name", max_length=255, unique=True)
    description = models.TextField(verbose_name="Movie Description")
    likes = models.IntegerField(default=0, null=True)
    rate = models.PositiveIntegerField(default=0)
    Production_date = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    # banner = models.ImageField(upload_to='movie/images')

    def __str__(self):
        return self.name
