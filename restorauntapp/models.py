from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    title = models.CharField(max_length=100)


class Food(models.Model):

    title = models.CharField(max_length=100)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    food_pic = models.ImageField(upload_to="food_pics/", null=True, blank=True)

    class Meta:
        ordering = [
            "category"
        ]