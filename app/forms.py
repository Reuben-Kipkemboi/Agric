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