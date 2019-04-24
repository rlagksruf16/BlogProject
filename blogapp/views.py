from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    posts = Blog.objects
    return render(request, 'home.html', {"posts": posts})

def detail(request, detail_id):
    post = get_object_or_404(Blog, pk=detail_id)
    return render(request, 'detail.html', {'post': post})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['subject']
    blog.body = request.POST['content']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, detail_id):
    destroy = get_object_or_404(Blog, pk=detail_id)
    destroy.delete()
    return redirect('home')

def update(request, detail_id):
    texts = get_object_or_404(Blog, pk=detail_id)
    return render(request, 'update.html', {'texts': texts})

def edit(request, detail_id):
    edit = Blog.objects.get(pk=detail_id)
    edit.title = request.POST['subject']
    edit.body = request.POST['content']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')