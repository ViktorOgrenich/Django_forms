from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def products(request):
    return render(request, 'blog/products.html', {})

def accounts(request):
    return render(request, 'blog/accounts.html', {})



