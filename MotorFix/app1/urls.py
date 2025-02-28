"""
URL configuration for MotorFix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from app1 import views

urlpatterns = [
   
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('login/view-items/', views.view_items, name='view-items'),  
    path('add/', views.add_items, name='add-items'),
    path('remove/<int:pk>/', views.delete_items, name='delete-items'),
   
    path('edit/<int:pk>/',views.update_items, name='update-items'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
