from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from .models import Task as TaskModel


def index(request):
    tasks = TaskModel.objects.all()
    if request.method == "POST":
        Task = request.POST.get('Task')
        Description = request.POST.get('Description')
        Priority = request.POST.get('Priority')
        NewTask = TaskModel(Task=Task, Description=Description, Priority=Priority,
                            Init_Date=str(datetime.now())[:10].replace('-', '/'),
                            Deadline_Date=str(datetime.now() + timedelta(days=5))[:10].replace('-', '/'))
        NewTask.save()
        return redirect('index')
    return render(request, 'Index.html', {'tasks': tasks})
