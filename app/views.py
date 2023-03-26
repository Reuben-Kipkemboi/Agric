from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

# APPLICATION VIEWS.
# home function
def home(request):
    comments= Feedback.objects.all()
    return render(request, 'public/index.html', {'comments':comments})


def services(request):
    machineries = Machinery.objects.all()
    return render(request, 'public/services.html', {'machineries': machineries})


# Register function

def public_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'logins/register.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request, 'logins/admin.html')


#user login
def user_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_owner:
                login(request, user)
                return redirect('owner')
            elif user is not None and user.is_public:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            else:
                msg= 'invalid credentials'
        else:
            messages.info = 'error validating form'
    return render(request, 'logins/login.html', {'form': form, 'msg': msg})

#admin
def admin(request):
    return render(request,'admin.html')


# logout function


def user_logout(request):
    logout(request)
    return render(request, 'public/index.html')


def profile(request):
    users = User.objects.all()
    current_user = request.user
    # profile = get_object_or_404(Profile,user=request.user)

    return render(request, 'profile/profile.html', {"users": users})


def update_profile(request):
    # profiles= Profile.objects.get(user=request.user)
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

# owners html
def owners(request):
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


def single_machine(request, machinery_id):
    single_machines = Machinery.objects.get(id=machinery_id)
    current_user = request.user
    user = User.objects.get(username=current_user.username)
    orders = Order.get_orders(machinery_id)

    return render(request, 'owners/single_machinery.html', {'single_machines': single_machines,'orders':orders})


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
        form2 = MachineryUpdateForm(instance=update)
    return render(request, 'owners/update_machinery.html', {'form2': form2})


def user_single_machine(request, machinery_id):
    single_machine = Machinery.objects.get(id=machinery_id)
    current_user = request.user
    user = User.objects.get(username=current_user.username)

    return render(request, 'public/single_machine.html', {'single_machine': single_machine})

def owner_single_machine(request, machinery_id):
    single_machine = Machinery.objects.get(id=machinery_id)
    current_user = request.user
    user = User.objects.get(username=current_user.username)

    return render(request, 'public/single_machine.html', {'owner_single_machine': single_machine})


def comment(request, machinery_id):
    current_user = request.user
    user = User.objects.get(username=current_user.username)
    machine = Machinery.objects.get(id=machinery_id)
    form2 = CommentForm()
    
    if request.method == 'POST':
        form2 = CommentForm(request.POST)
        if form2.is_valid():

            comment = form2.save(commit=False)

            comment.user_id = user
            comment.machinery_id = machine

            comment.save()

            return redirect('single_machine',machinery_id)
        else:
            form2 = CommentForm()

    return render(request, 'public/comment.html', {'form2': form2, 'machine': machine})


#order form
def order(request, machinery_id):
    current_user = request.user
    user = User.objects.get(username=current_user.username)
    machine = Machinery.objects.get(id=machinery_id)
    form3 = OrderForm()
    
    if request.method == 'POST':
        form3 = OrderForm(request.POST)
        if form3.is_valid():

            order = form3.save(commit=False)

            order.user_id = user
            order.machinery_id = machine

            order.save()

            return redirect('single_machine',machinery_id)
        else:
            form3 = OrderForm()

    return render(request, 'public/order.html', {'form3': form3, 'machine': machine})
