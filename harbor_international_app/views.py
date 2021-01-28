from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from login_app.models import *

def index(request):

    return render(request, "index.html")

def courses(request):
    if 'user_id' in request.session:

        context = {
            "user": User.objects.get(id = request.session['user_id']),
           # "snacks": Snack.objects.annotate(Count('likes')).order_by('-likes__count')
        }

        return render(request, "courses.html", context)
    else:
        return redirect('/user/signup') #login page
