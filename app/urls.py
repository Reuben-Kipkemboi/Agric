
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('signup/', views.base_register, name='signup'),
    
    
    path('public_register/', views.public_register, name='register'),
    
    path('owner_register/', views.owner_register, name='owner_register'),
    
    
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('profile/', views.profile, name='profile'),
    
    path('update_profile/', views.update_profile, name ='update'),
    
    path('owner_home/', views.owners, name='owner'),
    
]
