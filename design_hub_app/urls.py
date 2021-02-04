from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login_page), 
    url(r'^home$', views.home_page, name='homepage')
]
