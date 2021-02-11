from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Guest, GuestForm
from django.db.models import Q

# Create your views here.
def get_queryset(request): 
    if request.method== "POST":
        query = request.POST.get('search_guests')
        print(query)
        return Guest.objects.filter(
            Q(name__icontains=query))
    return Guest.objects.all()    

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    all_guests =  get_queryset(request);
    return render(request,'design_hub_app/homepage.html', {'guests' : all_guests })


def login_page(request):  
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    
    if user is not None:
        login(request, user)
        
        return redirect('/home')    
    else:  
        if request.method == "POST":
            context = { 'message': 'Please login with right credentials' }
            return render(request, 'design_hub_app/login.html',context= context )       
        return render(request, 'design_hub_app/login.html')       


# Add new guest
def add_new_guest(request):
    submitted = False

    if request.method == 'POST':
        form = GuestForm(request.POST)
        
        if form.is_valid():
             form.save()
             return redirect('/add_new_guest/?submitted=True')
    else:
        form = GuestForm()
        if 'submitted' in request.GET:
             submitted = True 
    return render(request, 'design_hub_app/add_new_guest.html', {'form': form, 'submitted': submitted})
def edit(request, id):  
    guest = Guest.objects.get(id=id)  
    return render(request,'design_hub_app/edit.html', {'guest':guest})  
def update(request, id):  
    guest = Guest.objects.get(id=id)  
    form = GuestForm(request.POST, instance = guest)  
    if form.is_valid():  
        form.save()  
        return redirect("/home")  
    return render(request, 'design_hub_app/edit.html', {'guest': guest, 'form': form})  
def destroy(request, id):  
    guest = Guest.objects.get(id=id)  
    guest.delete()  
    return redirect("/home") 
 