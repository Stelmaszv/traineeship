"""traineeship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app.views import AbstractView, KilometresPerHourViev, FootPerHourViev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',AbstractView.as_view(),name="main"),                                   #url for set type of conversion
    path('kilometresperhourviev/',KilometresPerHourViev.as_view(),name="kilometr" ),    #url for Kilometres per hour to fot per hour
    path('FootPerHourViev/',FootPerHourViev.as_view(),name="Foot" )               #url for foot per hour to fot per hour
]
