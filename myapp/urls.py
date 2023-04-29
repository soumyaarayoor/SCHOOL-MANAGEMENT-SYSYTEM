"""
URL configuration for myproject project.

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
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('teacherlogin',views.teacherlogin,name='teacherlogin'),
    path('studentsignup',views.studentsignup,name='studentsignup'),
    path('teachersignup',views.teachersignup,name='teachersignup'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('logout',views.logout,name='logout'),
    path('admin-page/', views.admin_page, name='admin_page'),

]
