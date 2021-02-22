from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from login_app.models import *
from .models import Item, Video, Algebra, Geometry
from .forms import Video_form, Algebra_form, Geometry_form


def index(request):
    all_video = Video.object.all()

    if request.method == "POST":
        form = Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        form = Video_form()
    return render(request, "index.html", {"form": form, "all":all_video})


def videoForm(request):
    context = {
        'form': Video_form,
        'algebraform': Algebra_form,
        'geometryform': Geometry_form,
        'videos': Video.objects.all(),
        'algebra': Algebra.objects.all(),
        'geometry': Geometry.objects.all()
    }
    return render(request, 'videos.html', context)

def uploadvideo(request):
    if request.method == "POST":   
        form = Video_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    
    return redirect('/video_form')

def uploadalgebra(request):
    if request.method == "POST":   
        form = Algebra_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    
    return redirect('/video_form')

def uploadgeometry(request):
    if request.method == "POST":   
        form = Geometry_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    
    return redirect('/video_form')


def courses(request):
    if 'user_id' in request.session:

        context = {
            "user": User.objects.get(id = request.session['user_id']),
            'videos': Video.objects.all(),
            'algebra': Algebra.objects.all(),
            'geometriesUnit1': Geometry.objects.filter(id__gt=0, id__lt=3),
            'geometriesUnit2': Geometry.objects.filter(id__gt=2, id__lt=6)
           # "snacks": Snack.objects.annotate(Count('likes')).order_by('-likes__count')
        }

        return render(request, "courses.html", context)
    else:
        return redirect('/user/signup') #login page

def geometry_material(request, course_id):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        'geometriesUnit1': Geometry.objects.filter(id__gt=0, id__lt=3),
        'geometriesUnit2': Geometry.objects.filter(id__gt=2, id__lt=6),
        'geometry': Geometry.objects.filter(id=course_id)
    }
    return render(request, "material.html", context)

def delete_video(request, video_id):
    delete_ = Snack.objects.get(id=snack_id)
    if delete_snack.publisher.id == request.session['user_id']:
        delete_snack.delete()

    return redirect('/snacks')
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
