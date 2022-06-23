from django import forms
from . models import *

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
#machinery update form
class MachineryUpdateForm(forms.ModelForm):
    class Meta:
        model = Machinery
        exclude = ['owner_id']
     
#comments form
class CommentForm(forms.ModelForm):
     class Meta:
        model = Feedback
        fields=['user_name','email', 'content', 'rating']
        
class OrderForm(forms.ModelForm):
     class Meta:
        model = Order
        exclude=['user_id','machinery_id']