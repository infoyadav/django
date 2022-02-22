from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=156)
    logo = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return str(self.name)

class Store(models.Model):
    name = models.CharField(max_length=30)    
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    class Meta:
        default_permissions = ('add',)
        permissions = (('give_refund','Can refund customers'),('can_hire','Can hire employees'), ('see_store','Customer See Store'))

# this is for create Elasticsearch
# class Category(models.Model):
#     name = models.CharField(max_length=30)
#     desc = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return '%s' % (self.name)


class Car(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])