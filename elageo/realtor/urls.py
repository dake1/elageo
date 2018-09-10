"""elageo URL Configuration

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
app_name = 'realtor'

from django.urls import path
from . import views
urlpatterns = [
    path('rent_list/',views.rent_list,name='rent_list'),
    path('rent_detail/<int:id>',views.rent_detail,name='rent_detail'),
    path('sale_list/',views.sale_list,name='sale_list'),
    path('sale_detail/<int:id>',views.sale_detail,name='sale_detail'),
    path('viewing_request/<int:pid>',views.viewing_request,name='viewing_request'),
    path('viewing_reqeust_sent', views.viewing_request_sent,name='viewing_request_sent'),
]
