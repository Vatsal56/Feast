from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class food_item(models.Model):
    name = models.CharField(max_length=264)
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class drink_item(models.Model):
    name = models.CharField(max_length=264)
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class table(models.Model):
    table_num = models.IntegerField(default=0)
    is_occupied = models.BooleanField(default=False)
    seats = models.IntegerField(default=0)
