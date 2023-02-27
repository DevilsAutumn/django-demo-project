from django.db import models


class Tires(models.Model):
    brand=models.TextField(max_length=10)
    size=models.IntegerField(default=16)

# Create your models here.
class dummy(models.Model):
    name=models.CharField(max_length=20)
    dummyfield = models.ForeignKey(Tires,on_delete=models.CASCADE)
    m2mfield=models.ManyToManyField(Tires,related_name="dummym2m")

