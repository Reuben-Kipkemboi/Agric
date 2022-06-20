from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# APPLICATION VIEWS.

#home function
def home(request):
    return render (request, 'index.html')

#Register function
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"check your passwords")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        return redirect ('login') 
    return render (request, 'register.html')


#Login function
def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("home")
    return render (request, 'login.html')

#logout function
def user_logout(request):
    return render (request, 'login.html')

