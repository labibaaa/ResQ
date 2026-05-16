"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', include('users.urls')),
    path('aid/', include('aid.urls')),
    #path('guide/', include('guide.urls')),
    #path('contacts/', include('contacts.urls')),
<<<<<<< HEAD
    #path('evacuation/', include('evacuation.urls')),
    path('incidents/', include('incidents.urls')),
=======
    path('evacuation/', include('evacuation.urls')),
>>>>>>> 8ed3885f560cb79666e7d40e9fe4727a995c348b
]