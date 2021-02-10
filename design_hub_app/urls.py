from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'), 
    url(r'^home$', views.home_page, name='homepage'),
    url(r'^add_new_guest/$', views.add_new_guest, name='add-new-guest'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]
