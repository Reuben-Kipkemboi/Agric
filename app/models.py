from importlib import machinery
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     is_owner = models.BooleanField(default=False)
#     is_public = models.BooleanField(default=False)

# class Owner(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)




#Application modules
# class User(AbstractUser):
#     is_public = models.BooleanField(default=False)
#     is_owner = models.BooleanField(default=False)


# class Owner(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     phone_number = models.CharField(max_length=20)
#     location = models.CharField(max_length=20)

# class Public(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     phone_number = models.CharField(max_length=20)
#     designation = models.CharField(max_length=20)
    
    # def __str__(self):
    #     return self.first_name    
    
    
 
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    # fullname=models.CharField(max_length=100,blank=True,null=True)
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
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile
 
    
class Machinery(models.Model):
    image=CloudinaryField('image', null=True)
    machinery_properties = models.TextField(null=True)
    machinery_name =models.CharField(max_length=50 , null=True)
    current_location = models.CharField(max_length=100, null=True)
    hire_price= models.IntegerField(default=0)
    ploughing_pay_rate= models.IntegerField(default=0)
    planting_pay_rate= models.IntegerField(default=0)
    forklifting_pay_rate= models.IntegerField(default=0)
    transport_pay_rate= models.IntegerField(default=0)
    operator_name = models.CharField(max_length=50 , null=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    def save_machinery(self):
        self.save()

    def update_machinery(self):
        self.update()

    def delete_farm(self):
        self.delete()
        
    @classmethod
    def find_machinery(cls,machinery_id):
        new_machinery = cls.objects.filter(machinery_id=machinery_id)
        return new_machinery

    def __str__(self):
        return self.machinery_name
    
    
class Owner_post(models.Model):
    machinery_name=models.CharField(max_length=100,null=True,blank=True)
    machinery_image=CloudinaryField('machinery_image',blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post",null=True,blank=True)
    describe=models.TextField(null=False)
    posted_at=models.DateTimeField(auto_now_add=True,)
    pay_rate=models.CharField(max_length=100,null=True,blank=True)

    def save_owner_post(self):
        self.save()

    def delete_owner_post(self):
        self.delete()

    def update_owner_post(self,id,owner_post):
        updated_post=Owner_post.objects.filter(id=id).update(owner_post)
        return updated_post


    def __str__(self):
        return self.machinery_name
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    service=models.CharField(max_length=40, null=True)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()

    def update_order(self,id,order):
        updated_order=Order.objects.filter(id=id).update(order)
        return updated_order


    def __str__(self):
        return self.machinery_name
    
class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_id =models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    
class Feedback(models.Model):
    content=models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    