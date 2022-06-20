from django.shortcuts import render, redirect

# APPLICATION VIEWS.

#home function
def home(request):
    return render (request, 'index.html')

#Register function
def register(request):
    return render (request, 'register.html')


#Login function
def user_login(request):
    return render (request, 'login.html')

#logout function
def user_logout(request):
    return render (request, 'login.html')

