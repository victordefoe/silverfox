"""DarkUnion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import sys

from django.contrib import admin
from django.urls import path, include

from researches import research


from django.http import HttpResponse
def index(request):
    return HttpResponse("这是首页")

# import research.views

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('researches/', include('researches.urls', namespace='researches'))
]
