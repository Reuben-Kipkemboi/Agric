from django.shortcuts import render, redirect

# Create your views here.


#home function
def home(request):
    return render (request, 'index.html')

#Register function
def register(request):
    return render (request, 'register.html')


#Login function
def user_login(request):
    return render (request, 'login.html')

