from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts=Post.objects.all()


    context = {
        "posts": posts,
        
    }
    
    

    return render(request, "posts/index.html", context)