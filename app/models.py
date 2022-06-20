from django.db import models
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


#Application modules
class Machinery(models.Model):
    image=CloudinaryField('image', null=True)
    machinery_properties = models.TextField(null=True)
    machinery_name =models.CharField(max_length=50 , null=True)
    current_location = models.CharField(max_length=100, null=True)
    hire_price= models.IntegerField(default=0)
    operator_name = models.CharField(max_length=50 , null=True)
    
    
    def __str__(self):
        return self.machinery_name
    
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.machinery_name
    
class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_id =models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    