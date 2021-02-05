from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Visitor

# Create your views here.

# Send a home_page with details of visitors
def home_page(request):
    all_visitors =  Visitor.objects.all();
    return render(request,'design_hub_app/homepage.html', {'visitors' : all_visitors })

# Send a login page 
def login_page(request):
   return render(request, 'design_hub_app/login.html')


