from django.shortcuts import get_object_or_404, render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# APPLICATION VIEWS.

#home function
def home(request):
    return render (request, 'index.html')


#base-register
def base_register(request):
    return render (request, 'base_register.html')


def public_register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"Check your passwords to make sure they match")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        return redirect ('login') 
    return render (request, 'register.html')

#Register function
def owner_register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"Check your passwords to make sure they match")
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
            messages.success(request,"Welcome ,you are now logged in")
            return redirect ("home")
    return render (request, 'login.html')

#logout function
def user_logout(request):
    return render (request, 'login.html')


def profile(request):
    users= User.objects.all()
    current_user = request.user
    # profile = get_object_or_404(Profile,user=request.user)
    
    return render (request, 'profile.html', {"users":users})


def update_profile(request):
    if request.method == 'POST':
        userprofileform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if  userprofileform.is_valid():
            userprofileform.save()
            return redirect(to='profile')
    else:
        form=ProfileUpdateForm(instance =request.user.profile)
    return render(request,'update_profile.html', {'form':form})



# def owners(request):
#     return render (request, 'owner.html')

#owners html
def owners(request):
    machinery=Machinery.objects.all()
    return render (request, 'owner_home.html',{'machinery':machinery})


def add_machinery(request):
    if request.method=='POST':
        image=request.FILES.get('image')
        describe=request.POST.get('describe')
        name =request.POST.get('name')
        neighbourhood_location=request.POST.get('location')
        occupants_count=request.POST.get('count')
        health_contacts=request.POST.get('contact')
        police_contacts=request.POST.get('police') 
        
        
        machinery=Machinery(image=image,describe=describe,name=name,neighbourhood_location=neighbourhood_location,health_contacts=health_contacts,police_contacts=police_contacts,
        occupants_count=occupants_count )
        
        # neighbourhoods.admin_id= request.user                      
        
        
        machinery.save_machinery()
        
        return redirect('owners')
    
    return render (request, 'add.html')

