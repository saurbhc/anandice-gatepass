"""GatePass URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',views.singIn, name='home_login'),
    #auth
    url(r'^postsign/',views.postsign, name='postsign'),
    url(r'^logout/',views.logout,name='log'),
    url(r'^signup/',views.signUp,name='signup'),
    url(r'^postsignup/',views.postsignup,name='postsignup'),
    #normal
    url(r'^normal/',views.normal,name='normal'),
    url(r'^normal_create/',views.normalCreate,name='normal_create'),
    url(r'^view_normal/',views.normalView,name='view_normal'),
    url(r'^post_view_normal/',views.postNormalView,name='post_view_normal'),
    #night
    url(r'^night/',views.night,name='night'),
    url(r'^night_create/',views.nightCreate,name='night_create'),
    url(r'^view_night/',views.nightView,name='view_night'),
    url(r'^post_view_night/',views.postNightView,name='post_view_night'),
    #emergency
    url(r'^emergency/',views.emergency,name='emergency'),
    url(r'^emergency_create/',views.emergencyCreate,name='emergency_create'),
    url(r'^view_emergency/',views.emergencyView,name='view_emergency'),
    url(r'^post_view_emergency/',views.postEmergencyView,name='post_view_emergency'),
]
