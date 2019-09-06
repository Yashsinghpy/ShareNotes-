"""socialproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from socialapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.registration,name='registration'),
    path('note/',views.note,name='note'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('check/',views.check,name='check'),
     path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('share/<int:id>/<str:name>/',views.share,name='share'),
    
    
]
