from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'), 
    url(r'^home$', views.home_page, name='homepage'),
    url(r'^add_new_visitor/$', views.add_new_visitor, name='add-new-visitor')
]
