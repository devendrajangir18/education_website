from datetime import datetime as dt

from bson.objectid import ObjectId
from django.shortcuts import redirect, render
from django.contrib import messages
from edupro.settings import db


# Create your views here

def postcommit(request):
    if request.method == 'POST':
        title = request.POST['title'] 
        content = request.POST['content']
        username = request.POST['username']
        timeStamp = dt.now()

        db.blogpost.insert_one({"title":title , "content": content, "username": username, "timeStamp": timeStamp})
        # post = {"title":title ,"content": content, "username": username, "timeStamp": timeStamp}

        return redirect(f'/ucommit/post/',)


    else:
        posts = db.blogpost.find()
        posts = {"posts": posts, }

        return render(request, "post.html", posts)


def post_page(request, post_id):
    if request.method == 'POST':
        content = request.POST['content']
        name = request.POST['name']
        timeStamp = dt.now()

        # if request.user.is_authenticated:    
        #     db.users.find_one({"username" : username})

        db.usercom.insert_one({"post_id": post_id, "content": content, "name": name, "timeStamp": timeStamp})
        return redirect(f'/ucommit/post/{post_id}')
    
    # else:
        #     messages.info(request, 'user not registered')
        #     return redirect('postcommit')
            

    else:
        post = db.blogpost.find_one({"_id": ObjectId(post_id)})
        comments = db.usercom.find({"post_id": post_id})

        context = {"post": post, "comments": comments, "post_id": post_id}

        return render(request, "postcommit.html", context)
    



        
    