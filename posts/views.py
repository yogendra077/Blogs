from django.shortcuts import render
from .models import Post
def index(request):
    post=Post.objects.all()
    return render(request,'index.html', {'posts' : post} )

def post(request,id):
    post=Post.objects.get(id = id)
    return render(request,'post.html', {'post' : post} )
