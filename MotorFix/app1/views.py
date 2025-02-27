from django.shortcuts import render

# Create your views here.
def ProfilePage(request):
    return render(request,'profile.html')

def SignupPage(request):
    return render(request,'signup.html')

def LoginPage(request):
    return render(request,'login.html')