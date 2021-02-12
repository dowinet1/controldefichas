from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.core import serializers
from django.contrib.auth.hashers import check_password
import json
import smtplib
import sweetify
import datetime


def index(request):
    return render(request, "index.html", {
    
    })
def panel(request):
    return render(request, "menu/basepanel.html", {
    
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('')
    return render(request,"login.html", {
       
    })

def inicio(request):
    return render(request, "login.html", {
       
    })

def excel(request):
    return render(request, "excel.html",{
         "message ": "hola viasat",
    })

def contac(request):
    return render(request, "contact.html")
