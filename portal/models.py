
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.enums import Choices, ChoicesMeta, IntegerChoices, TextChoices
#from django.db.models.enums import IntegerChoices
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
class City(models.Model):
    name=CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class Area(models.Model):
    name=CharField(max_length=30)
    city=models.ForeignKey(City,on_delete=CASCADE)
    def __str__(self):
        return str(self.name)
       

class Pg(models.Model):
    name=CharField(max_length=30)
    address=CharField(max_length=150)
    location=models.URLField(max_length = 200)
    contact_number=PhoneNumberField(null=False, blank=False, unique=True)
    area=models.ForeignKey(Area,null=True,default=None,on_delete=SET_NULL)
    city=models.ForeignKey(City,null=True,default=None,on_delete=SET_NULL)
    food=IntegerField(choices=[(1,'north_indian'),(2,'south_indian'),(3,'both')],default=2,null=True,blank=True)
    pgtype=IntegerField(choices=[(1,'GENTS'),(2,'LADIES')],default=1,null=True,blank=True)
    description=TextField(null=True,blank=True)
    def __str__(self):
        return str(self.name)
class Images(models.Model):
    pg=models.ForeignKey(Pg,null=True,default=None,on_delete=models.SET_NULL)
    images=ImageField(upload_to='images')
    def __str__(self):
        return str(self.pg.name)
class Sharing_choice(models.IntegerChoices):
    single=1
    doulbe=2
    triple=3
    four=4
class Sharing(models.Model):
    sharing_cap=IntegerField(choices=Sharing_choice.choices)
    price=IntegerField()
    pg=models.ForeignKey(Pg,null=True,default=None,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.pg.name)