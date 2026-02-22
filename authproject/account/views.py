from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('login')
    return render(request,'register.html')
def Login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render (request,'login.html',{'error':'invalid Credentials'})
    return render(request,"login.html")
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def dashboard(request):
    return render(request,'dashboard.html')
