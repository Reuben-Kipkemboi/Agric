
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # path('signup/', views.base_register, name='signup'),
    
    
    path('public_register/', views.public_register, name='register'),
    
    # path('owner_register/', views.owner_register, name='owner_register'),
    
    
    path('login/', views.user_login, name='login'),
    
    path('admin/', views.admin, name='admin'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('profile/', views.profile, name='profile'),
    
    path('update_profile/', views.update_profile, name ='update'),
    
    path('owner_home/', views.owners, name='owner'),
    
    path('add_machinery/', views.add_machinery, name='add'),
    
    path('machinery/<int:machinery_id>/', views.single_machine, name='single'),
    
    path('update/<int:machinery_id>/details', views.update_machinery, name='update'),
    
    
    path('delete/<int:machinery_id>', views.delete_machinery, name='delete'),
    
    path('services/', views.services, name='services'),
    
    path('user_machinery/<int:machinery_id>/', views.user_single_machine, name='single_machine'),
    
    path('owner_machinery/<int:machinery_id>/', views.owner_single_machine, name='owner_single_machine'),
    
    path('comment/<int:machinery_id>', views.comment, name='comment'),
    
    path('hire/<int:machinery_id>', views.order, name='order'),
    
    
    
]
