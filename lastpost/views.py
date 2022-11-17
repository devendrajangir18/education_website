from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime as dt
from bson.objectid import ObjectId
from edupro.settings import db



# Create your views here.

def post_comment(request, post_id):
    if request.method == 'POST':
        post_title: request.POST['post_title']
        author: request.POST['author']
        content: request.POST['content']
        comment: request.POST['comment']
        timeStamp: dt.now()
        username: request.POST['username']
        text: request.POST['text']

        # if db.users.find_one({'username': username}):
        db.po_comment.insert_one({'post_title': post_title, 'author': author, 'content': content, 'comment': {'post_id': post_id, 'username': username, 'text': text, 'timeStamp': timeStamp}})

        return redirect(f'/lastpost/postblog/{post_id}')
        
        # else:
        #     messages.info(request, "First Login Please..!")
        #     return redirect('postblog')

    else:
        post = db.po_comment.find_one({"_id": ObjectId(post_id)})
        comments = db.po_comment.find({'post_id': post_id, 'comment': comment})

        context = {'post': post, 'comments': comments, 'post_id': post_id}

        return render(request, 'postblog.html', context)


    

