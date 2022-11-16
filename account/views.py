import re

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render

from edupro.settings import db

from .models import login, logout, register


def register(request):
    
    print(dir(request))
    print(request.method)
    print(request.META)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        # db.users.insert_one({'first_name': first_name, 'last_name':last_name, 'username': username, 'email': email, 'password': password1,})
        if password1 == password2:
            if db.users.find_one({"username" : username}):
                messages.info(request, 'username taken')
                return redirect('register')
            elif db.users.find_one({"email" : email}):
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                db.users.insert_one({'first_name': first_name, 'last_name':last_name, 'username': username, 'email': email, 'password': password1,})             
                messages.info(request, 'Registrations Successful. login Please!')
                return redirect('login')
        else:
            messages.info(request, 'Password Not matching')
            return redirect('register')
                 
    else:
        return render(request, 'register.html', {})


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        if db.users.find_one({"email": email, "password": password}):
            messages.info(request, 'logged in successfully')
            return redirect("/")
                     
        else:
            messages.info(request, 'Invalid Password !')
            return redirect("http://127.0.0.1:8000/account/login/")
        
    else:
        return render(request, 'login.html',{})

def logout(request):
    # if request.method == 'POST':
    #     email = request.POST['email']

    #     if db.users.find_one({"emial": email}):
            return redirect ('/')





















#for pymongo
        #outside part
        #def login(request):
        # print(dir(request))
        # print(request.method)
        # print(request.META)
        # print(request.data)

        #insidepart
        # db.users.insert_one({'email': email, 'password': password})

#  ek page se dusre page par redirect karne k liye urls mai given name ko pass krne hai
#  return redirect('login')

# for djongo 
        # password checking
                # if user.object.filter(username==username).exists():
        #else part
                # user = user.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                # user.save()