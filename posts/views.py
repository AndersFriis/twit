from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post 
from .forms import PostForm
from django.contrib.auth.models import User

def index(request):
    posts=Post.objects.all()
    users=User.objects.all()
    # objects.all() is saying that we what everything to show, so all posts and all forms  

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post= post.save()

            messages.success(request, "Post created!")
            return redirect("posts:index")
    else:
        form = PostForm()

    context = {
        "posts": posts,
        "form": form,
        "users": users,
        
    }
    
    

    return render(request, "posts/index.html", context)







    
