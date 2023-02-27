from django.shortcuts import render

from main.models import Post


# Create your views here.
def index(request):
    postlist=Post.objects.all()
    return render(request,'index.html', {'postlist':postlist})
def blog(request):
    postlist=Post.objects.all()
    return render(request,'blog.html',{'postlist':postlist})
def postdetails(request,pk):
    postlist=Post.objects.get(pk=pk)
    return render(request, 'postdetails.html', {'postlist':postlist})
