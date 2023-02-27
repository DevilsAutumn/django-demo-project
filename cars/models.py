from django.db import models

# Create your models here.
# class Tires(models.Model):
#     brand=models.TextField(max_length=10)
#     size=models.IntegerField(default=16)

class Cars(models.Model):
    name=models.TextField(max_length=20)
    model= models.CharField(max_length=10)
    price=models.IntegerField(default=0)
    tires=models.ForeignKey("tires.Tires",on_delete=models.CASCADE) 