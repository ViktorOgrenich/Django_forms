from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_home(request):
    novost = News.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'novost': novost})

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма заполнена неверно'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'news/create.html', data)