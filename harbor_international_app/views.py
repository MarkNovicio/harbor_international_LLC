from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):

    return render(request, "index.html")

def math_courses(request):
    return render(request, "math.html")