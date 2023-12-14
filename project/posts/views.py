from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import AddState

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', context={'posts': posts})

def create(request):
    if request.method == "POST":
        form = AddState()
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Post.objects.create(title=title, text=text)
            return redirect('home')
    return render(request, 'create.html', context={'form': form})

def update(request, id):
    try:
        men = Post.objects.get(id=id)
        if request.method == "POST":
            men.title = request.POST.get('title')
            men.text = request.POST.get('text')
            men.save()
            return redirect('home')
        else:
            return render(request, 'update.html', context={'men': men})
    except:
        return redirect('create')

def state(request, id):
    try:
        men = Post.objects.get(id=id)
        return render(request, 'state.html', context={'men': men})
    except:
        return redirect('')
