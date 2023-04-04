from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name=models.CharField(max_length=500)
    
    def __str__(self):
        return self.category_name

    class Meta:
        db_table="app_categories"

class Product(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.FileField(null=True, blank=True, upload_to='products/') # if *** folder doesnt already exist it creates folder *** in a new media folder
    quantity = models.IntegerField()
    discount =  models.FloatField()
    cash_on_delivery = models.CharField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        db_table="app_products"


    




# Create your models here.
