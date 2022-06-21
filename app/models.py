from django.db import models
# from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.contrib.auth.models import AbstractUser


#Application modules
class User(AbstractUser):
    is_public = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

class Public(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user    
    
    
 
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    fullname=models.CharField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    user_email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=CloudinaryField('image')
    biography=models.TextField(blank=True,null=True)
    contact_number=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def profile_update(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return str(self.username)
 
    
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
    