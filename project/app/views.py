from django.shortcuts import render, redirect
from .models import UserModel, Order
from datetime import datetime
from .forms import AddMen

def index(request, chel):
    people = UserModel.objects.order_by('-name', '-age')
    chel = UserModel.objects.latest()
    return render(request, 'posts/index.html', context={'people': people})

def create(request):
    if request.method == "POST":
        form = AddMen()
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            UserModel.objects.create(name=name, age=age)
            return redirect('home')
    return render(request, 'posts/create.html', context={'form': form})

def update(request, id):
    try:
        men = UserModel.objects.get(id=id)
        if request.method == "POST":
            men.name = request.POST.get('name')
            men.age = request.POST.get('age')
            men.save()
            return redirect('home')
        else:
            return render(request, 'posts/update.html', context={'men': men})
    except:
        return redirect('create')

def user(request, id):
    try:
        men = UserModel.objects.get(id=id)
        return render(request, 'posts/user.html', context={'men': men})
    except:
        return redirect('home')

def order(request):
    createOrders()
    orders = Order.objects.all()
    return render(request, 'posts/orders.html', context={'orders': orders})

def createOrders():
    if Order.objects.count() < 5:
        Order.objects.create(datetime=datetime(2020, 6, 23, 12, 23, 55))
        Order.objects.create(datetime=datetime(2023, 12, 8, 12, 23, 55))
        Order.objects.create(datetime=datetime(2022, 7, 15, 12, 23, 55))
        Order.objects.create(datetime=datetime(2021, 11, 20, 12, 23, 55))
        Order.objects.create(datetime=datetime(2023, 10, 21, 12, 23, 55))
