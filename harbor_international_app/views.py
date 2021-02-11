from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from login_app.models import *
from .models import Item, Video
from .forms import Video_form


def index(request):
    all_video = Video.object.all()

    if request.method == "POST":
        form = Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>uploded successfully")
    else:
        form = Video_form()
    return render(request, "index.html", {"form": form, "all":all_video})

def courses(request):
    if 'user_id' in request.session:

        context = {
            "user": User.objects.get(id = request.session['user_id']),
           # "snacks": Snack.objects.annotate(Count('likes')).order_by('-likes__count')
        }

        return render(request, "courses.html", context)
    else:
        return redirect('/user/signup') #login page

def admin(request):
    def create_registration(request):
    if request.method == 'GET':
        return redirect('/admin')

    else:
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            math = request.POST['math'],
            grade = request.POST['grade'],
            password = pw_hash
        )

        request.session['user_id'] = new_user.id
        request.session['first_name']= new_user.first_name
        request.session['last_name']= new_user.last_name
        request.session['email']= new_user.email
        request.session['grade']= new_user.grade
        request.session['math']= new_user.math
        # context = {
        #     "new_user_added": Registration.objects.get(id=request.session['user_id'])
        # }
        #i need to redirect not render
        return redirect('/')

    return render(request, "admin.html", context)

def video(request):
    obj = Item.object.all()
    return render(request, 'testimonials.html', {'obj':obj})
