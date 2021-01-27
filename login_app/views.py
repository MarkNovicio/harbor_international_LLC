from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):

    return render(request, "index.html")

def signup(request):

    return render(request, "sign_up.html")

def create_registration(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        #This code should render the error messages in the
        # Registration section
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)

        return redirect('/user/signup')
    
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].
        encode(), bcrypt.gensalt(rounds =13)).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )

        request.session['user_id'] = new_user.id
        request.session['first_name']= new_user.first_name
        request.session['last_name']= new_user.last_name
        request.session['email']= new_user.email
        # context = {
        #     "new_user_added": Registration.objects.get(id=request.session['user_id'])
        # }
        #i need to redirect not render
        return redirect('/')

def login_page(request):
    return render(request, "login.html")

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid email/password')
        return redirect('/')
    else:
        logged_users = User.objects.filter(email=request.POST['email'])
        user = logged_users[0]
        request.session['user_id'] = user.id
        request.session['first_name']= user.first_name
        request.session['last_name']=user.last_name
        request.session['email']= user.email

        #return render(request, "message_wall.html", context)
        return redirect('/snacks') #change this redirect to the page you want to redirect

def logout(request):
    del request.session['user_id']
    del request.session['first_name']
    del request.session['last_name']
    del request.session['email']

    #request.session.clear()
    return redirect('/')

    