from django.shortcuts import render

def addeducation(request):
    return render(request,'accounts/add-education.html',{})

def addexperience(request):
    return render(request,'accounts/add-experience.html',{})

def createprofile(request):
    return render(request,'accounts/create-profile.html',{})

def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

def login(request):
    return render(request,'accounts/login.html',{})

def profile(request):
    return render(request,'accounts/profile.html',{})

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def register(request):
    return render(request,'accounts/register.html',{})



# Create your views here.
