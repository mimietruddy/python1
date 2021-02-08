from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Visitor

# Create your views here.

# Send a home_page with details of visitors
def home_page(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    all_visitors =  Visitor.objects.all();
    return render(request,'design_hub_app/homepage.html', {'visitors' : all_visitors })

# Send a login page 
def login_page(request):  
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/home')    
    else:  
        if request.method == "POST":
            context = { 'message': 'Please login with right credentials' }
            return render(request, 'design_hub_app/login.html',context= context )       
        return render(request, 'design_hub_app/login.html')       
      