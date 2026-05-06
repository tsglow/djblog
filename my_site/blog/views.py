from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify

post_list = [
    {"date": "04-08", "title": "good day to die", "content": "good morning everyone, it is a good day to die"},
    {"date": "04-09", "title": "another day on earth", "content": "so I wake up once again, with a headache"},
    {"date": "04-10", "title": "RIP mushrooms", "content": "in the refrigerator, I have kept these guys for two months..."},
    {"date": "04-11", "title": "Time flys like an arrow", "content": "why time flys like an arrow, not a bunch of banana, or apple?"},
]
    
    


# Create your views here.

def index(request):    
    recents = post_list[-2:][::-1]    
    for r in recents:
        if r.get("url") is None:
            r["url"] = slugify(r["title"])    
    return render(request, "blog/index.html", {"recent": recents})


def posts(request):
    for p in post_list:
        if p.get("url") is None:
            p["url"] = slugify(p["title"])
    print(post_list)
    return render(request,"blog/posts.html", {"list": post_list} )


def read_post(request,url):
    try:        
        post = list(filter(lambda i : i['url'] == url, post_list))[0]            
        print(post)
        return render(request, "blog/post.html", {"post": post})       
    except:        
        raise Http404()