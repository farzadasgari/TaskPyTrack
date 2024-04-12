from datetime import datetime, timedelta

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Task as TaskModel


def index(request):
    tasks = TaskModel.objects.all()
    if request.method == "POST":
        Task = request.POST.get('Task')
        Description = request.POST.get('Description')
        Priority = request.POST.get('Priority')
        Deadline_Date = request.POST.get('Deadline_Date')
        NewTask = TaskModel(Task=Task, Description=Description, Priority=Priority,
                            Init_Date=str(datetime.now())[:10].replace('-', '/'),
                            Deadline_Date=Deadline_Date)
        NewTask.save()
        return redirect('index')
    return render(request, 'Index.html', {'tasks': tasks})


def delete_task(request, pk):
    task = TaskModel.objects.get(pk=pk)
    task.delete()
    return redirect('index')


def search_task(request):
    if request.method == "POST":
        search = request.POST.get('search')
        tasks = TaskModel.objects.filter(Q(Task__icontains=search) | Q(Description__icontains=search))
        return render(request, 'Index.html', {'tasks': tasks, 'search': search})
