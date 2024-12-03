from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Create the user
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])  # Set the password
            user.save()  
            
            # Authenticate the user
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user) 
                return redirect('dashboard')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):  
    error_message = ""  
    
    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)  
        
        if form.is_valid():  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username=username, password=password)  
            
            if user is not None:  
                login(request, user)  
                return redirect('dashboard')    
            else:  
                error_message = "Invalid username or password."  
                messages.error(request, error_message) 
        else:  
            error_message = "Invalid form submission." 
            messages.error(request, error_message)    
    
    else:  
        form = AuthenticationForm()  # Initialize form for GET request  

    return render(request, 'auth/login.html', {'form': form, 'error_message': error_message})  


def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
