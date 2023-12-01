from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, get_user_model



# Create your views here.

User = get_user_model

def signup(request):
    if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                    form.save()
                    return redirect("index")
            else:
                form = RegisterForm()
                return render(request, 'registrations/signup.html', {"form": form})
    return render(request, 'registrations/signup.html',{'form':RegisterForm})
        
                    
   
    return render(request, "registrations/signup.html")


def login(request):
   
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")
    return render(request, 'registrations/login.html')
           
  

