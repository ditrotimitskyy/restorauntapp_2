from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Food(models.Model):

    title = models.CharField(max_length=100)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    food_pic = models.ImageField(upload_to="food_pics/", null=True, blank=True)

    class Meta:
        ordering = [
            "category"
        ]
    def __str__(self):
        return self.title
    
class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=200)
    amount = models.IntegerField()
    datetime = models.DateField(auto_now_add=True)