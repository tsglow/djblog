from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify

posts = [
    {"date": "04-08", "title": "good day to die", "content": "good morning everyone, it is a good day to die"},
    {"date": "04-09", "title": "another day on earth", "content": "so I wake up once again, with a headache"},
    {"date": "04-10", "title": "RIP mushrooms", "content": "in the refrigerator, I have kept these guys for two months..."},
    {"date": "04-11", "title": "Time flys like an arrow", "content": "why time flys like an arrow, not a bunch of banana, or apple?"},
]
    
    


# Create your views here.

def index(request):
    for p in posts:
        if p.get("url") is None:
            p["url"] = slugify(p["title"])
    print(posts)
    return render(request,"blog/index.html", {"list": posts} )


def read_post(request,url):
    try:        
        post = list(filter(lambda i : i['url'] == url, posts))[0]            
        print(post)
        return render(request, "blog/post.html", {"post": post})       
    except:        
        raise Http404()