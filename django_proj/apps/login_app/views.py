from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    show_user = User.objects.all()
    context = {
        "html_show_user": show_user,
    }
    print(show_user)
    return render(request,'login_app/login.html', context)

def register(request):    
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            hashed_password = hashed_password.decode('utf-8')
            print(type(hashed_password))
            print(hashed_password)
            new_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],password=hashed_password)
            print(new_user)
            request.session['user_id'] = new_user.id
            messages.error(request, "You have successfully registered")
            return redirect('/')
    return redirect('/')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"])
        except:
            messages.error (request, "Username or password is invalid")
            return redirect('/')
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['email'] = user.email
            request.session['user_id'] = user.id
            request.session['user_firstname'] = user.first_name
            request.session['user_lastname'] = user.last_name
            return redirect('/users/success')
        else:
            messages.error (request, "Username or password is invalid")
            return redirect('/')
    return redirect('/')

def success(request):
    return redirect('/home')
       
def logout(request):
    request.session.clear()
    messages.error(request, "You have successfully logged out")
    return redirect('/')    
