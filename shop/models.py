from django.db import models

# Create your models here
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default='')
    subcategory = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images',default='')

    def __str__(self) -> str:
        return self.product_name 

class Contact(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default='')
    phoneNo = models.CharField(max_length=100,default='')
    query = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name 

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=100000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.update_desc[0:7]+'...'