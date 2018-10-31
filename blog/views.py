from django.shortcuts import render
from blog.models import Post

# Create your views here.


def post_list(request):
    post=Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts':post})

def open_blog(request,second):
    return render(request,'blog/open_blog.html',{})
