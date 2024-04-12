from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Task as TaskModel, Track


def index(request):
    tracks = Track.objects.all()
    if request.method == "POST":
        Task = request.POST.get('Task')
        Description = request.POST.get('Description')
        Priority = request.POST.get('Priority')
        Deadline_Date = request.POST.get('Deadline_Date')
        NewTask = TaskModel(Task=Task, Description=Description, Priority=Priority,
                            Init_Date=str(datetime.now())[:10].replace('-', '/'),
                            Deadline_Date=Deadline_Date)
        NewTask.save()
        NewTrack = Track(Checklist=NewTask)
        NewTrack.save()
        return redirect('index')
    return render(request, 'Index.html', {'tracks': tracks})


def delete_task(request, pk):
    track = Track.objects.get(pk=pk)
    track.delete()
    return redirect('index')


def search_task(request):
    if request.method == "POST":
        search = request.POST.get('search')
        tracks = Track.objects.filter(Q(Checklist__Task__icontains=search) | Q(Checklist__Description__icontains=search))
        return render(request, 'Index.html', {'tracks': tracks, 'search': search})


def edit_task(request, pk):
    if request.method == "POST":
        Edit_Task = request.POST.get('Edit_Task')
        Edit_Description = request.POST.get('Edit_Description')
        Edit_Priority = request.POST.get('Edit_Priority')
        Edit_Deadline_Date = request.POST.get('Edit_Deadline_Date')
        MyTrack = Track.objects.get(pk=pk)
        MyTrack.Checklist.Description = Edit_Description
        MyTrack.Checklist.Priority = Edit_Priority
        MyTrack.Checklist.Deadline_Date = Edit_Deadline_Date
        MyTrack.Checklist.Task = Edit_Task
        MyTrack.Checklist.save()
        MyTrack.save()
        return redirect('index')
