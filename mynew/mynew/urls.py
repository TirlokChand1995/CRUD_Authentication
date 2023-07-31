"""
URL configuration for myauth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Signup',views.Signup,name="signup"),
    path('',views.Login,name='login'),
    path('Logout/',views.LogoutPage,name='logout'),
    path('Home/', views.Index,name="home"),
    path('Add/',views.Add,name="add"),
    path('Edit/',views.Edit,name="edit"),
    path('Update/<str:id>',views.Update,name="update"),
    path('Delete/<str:id>',views.Delete,name="delete")
]
