"""
URL configuration for PathwayPro_Project project.

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
from django import views
from django.contrib import admin
from django.urls import path, include
# from Pathway_App.views import chat

from Pathway_App.views import home, response_view, noc_Result
import Pathway_App.views
from captcha import urls as captcha_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/chat/', chat, name='chat'),
    path('', home, name='home'),
    path('home/', home, name='home1'),
    path('response/<str:response>/', response_view, name='response'),
    path('noc_result/', noc_Result, name='noc_result'),  # Updated view name to 'noc_result'
    path('', include(captcha_urls)),
]


