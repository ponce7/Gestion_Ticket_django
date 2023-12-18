from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout, get_user_model

from django.contrib.auth.decorators import login_required

# Create your views here.


User = get_user_model()
def signup(request):
    if request.method == "POST":
            username = request.POST.get("username")
            
            password = request.POST.get("password")
            User.objects.create_user(username=username, password=password)
            return redirect('connexion')
    
    return render(request, 'accounts/signup.html',{'form':RegisterForm})
        
def connexion(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            logged_user = User.objects.get(username=username)
            request.session['logged_user.id'] = logged_user.id
            login(request, user)

            return redirect("index")
    return render(request, 'accounts/login.html')
           
  
def deconnexion(request):
     logout(request)
     return redirect('index')