"""
URL configuration for geeks project.

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

from django.contrib import admin
from django.urls import path, include
from geeks.tutorials import views


from django.contrib.auth import views as auth



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorials.urls')),
    path('login/', views.login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name = 'templates/home'), name='logout'),
    path('register/', views.register, name='register'),

]
