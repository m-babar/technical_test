"""technical_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers


from pets import views as api_views
# from api_test import views as test_views
# router = routers.DefaultRouter()
# router.register(r'pets', views.PetView, base_name='pets')

urlpatterns = [

    #API urls
    url(r'^signup/', api_views.Signup.as_view(), name='signup' ),
    url(r'^login/', api_views.Login.as_view(), name='login' ),
    url(r'^logout/', api_views.Logout.as_view(), name='logout' ),

    url(r'^pets/$', api_views.PetView.as_view(), name='pets'),
    url(r'^pets/(?P<pk>[0-9]+)/$', api_views.PetView.as_view(), name='pets'),

]
