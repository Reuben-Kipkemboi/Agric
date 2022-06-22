from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required


# APPLICATION VIEWS.

#home function
def home(request):
    return render(request, 'public/index.html')


#base-register
def base_register(request):
    return render(request, 'logins/base_register.html')


def public_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(
                request, "Check your passwords to make sure they match")
            return redirect('/register')

        new_user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password1)

        new_user.save()
        return redirect('login')
    return render(request, 'logins/register.html')

#Register function


def owner_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(
                request, "Check your passwords to make sure they match")
            return redirect('/register')

        new_user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password1)

        new_user.save()
        return redirect('login')
    return render(request, 'logins/register.html')


#Login function
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome ,you are now logged in")
            return redirect("home")
    return render(request, 'logins/login.html')

#logout function


def user_logout(request):
    logout(request)
    return render(request, 'public/index.html')


def profile(request):
    users = User.objects.all()
    current_user = request.user
    # profile = get_object_or_404(Profile,user=request.user)

    return render(request, 'profile/profile.html', {"users": users})


def update_profile(request):
    if request.method == 'POST':
        userprofileform = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if userprofileform.is_valid():
            userprofileform.save()
            return redirect(to='profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile/update_profile.html', {'form': form})


# def owners(request):
#     return render (request, 'owner.html')

#owners html
def owners(request ):
    machinery = Machinery.objects.all()
    return render(request, 'owners/owner_home.html', {'machinery': machinery})


def add_machinery(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        machinery_properties = request.POST.get('describe')
        machinery_name = request.POST.get('machine')
        current_location = request.POST.get('location')
        availability = request.POST.get('available')
        hire_price = request.POST.get('hire')
        ploughing_pay_rate = request.POST.get('ploughing')
        forklifting_pay_rate = request.POST.get('forklifting')
        transport_pay_rate = request.POST.get('transport')
        planting_pay_rate = request.POST.get('planting')
        operator_name = request.POST.get('operator_name')

        machinery = Machinery(image=image, machinery_properties=machinery_properties, machinery_name=machinery_name, current_location=current_location, availability=availability, hire_price=hire_price, ploughing_pay_rate=ploughing_pay_rate,
                              forklifting_pay_rate=forklifting_pay_rate, transport_pay_rate=transport_pay_rate, planting_pay_rate=planting_pay_rate, operator_name=operator_name)

        machinery.owner_id = request.user

        machinery.save_machinery()

        return redirect('owner')

    return render(request, 'owners/add.html')

def single_machine(request, machinery_id ):
    single_machines=  Machinery.objects.get(id=machinery_id)
    current_user = request.user
    user = User.objects.get(username=current_user.username)
    
    return render(request, 'owners/single_machinery.html', {'single_machines':single_machines})

def delete_machinery(request, machinery_id):
  machinery = Machinery.objects.get(id=machinery_id)
  machinery.delete()
  return redirect('owner')


def update_machinery(request, machinery_id):
    update = Machinery.objects.get(id=machinery_id)
    if request.method == 'POST':
        machineryform = MachineryUpdateForm(
            request.POST, request.FILES, instance=update)
        if machineryform.is_valid():
            machineryform.save()
            return redirect('single', machinery_id)
    else:
        form2 = MachineryUpdateForm(instance=update )
    return render(request, 'owners/update_machinery.html', {'form2': form2})



