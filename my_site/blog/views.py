from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from .models import Author, Post
from datetime import date


post_list = [
    {"date": date(2026,4,11), "author": "max", "title": "Time flys like an arrow", "image": "mountains.jpg","content": "why time flys like an arrow, not a bunch of banana, or apple?"},
    {"date": date(2026,4,9), "author": "max", "title": "another day on earth", "image": "mountains.jpg", "content": "so I wake up once again, with a headache"},
    {"date": date(2026,4,8), "author": "max", "title": "good day to die", "image": "mountains.jpg", "content": "good morning everyone, it is a good day to die"},    
    {"date": date(2026,4,10), "author": "max", "title": "RIP mushrooms", "image": "mountains.jpg", "content": "in the refrigerator, I have kept these guys for two months..."},    
]
    
def get_date(post):
    return post.get("date")


# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-date")            
    print(posts)  
    recents = posts[:2]        
    return render(request, "blog/index.html", {"recent": recents})


def posts(request):
    posts = Post.objects.all().order_by("-date")    
    return render(request,"blog/posts.html", {"list": posts} )


def read_post(request,url):
    try:   
        post = Post.objects.get(url=url)
        return render(request, "blog/post.html", {"post": post})       
    except:        
        raise Http404()