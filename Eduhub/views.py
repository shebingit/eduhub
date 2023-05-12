from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth


# User section 

def HomePage(request):
    return render(request, 'user/index.html')

def AboutPage(request):
    return render(request, 'user/about.html')

def CoursePage(request):
    return render(request, 'user/course.html')

def PlacementPage(request):
    return render(request, 'user/placement.html')

def ContactPage(request):
    return render(request, 'user/contact.html')


def RegisterForm(request):
    return render(request, 'user/registerform.html')






