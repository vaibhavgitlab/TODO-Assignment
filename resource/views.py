from django.shortcuts import render, redirect
from .models import Todos
# Create your views here.


def home(request):
    tasks = Todos.objects.all()
    return render(request, 'index.html',{"tasks":tasks})

def create(request):
    if request.method == 'POST':
        task = request.POST['task']
        status = request.POST['status']
        Todos.objects.create(task=task, status=status)
        return redirect('home')
    return render(request, 'create.html')

def update(request,pk):
    s = Todos.objects.get(id = pk)
    if request.method == 'POST':
        task = request.POST['task']
        status = request.POST['status']
        s.task = task
        s.status = status
        s.save()
        return redirect('home')
    return render(request, 'update.html',{"s":s})