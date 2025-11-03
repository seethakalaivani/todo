from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task


# Create your views here.
def addTask(request):
    #print(request.POST) # to take the task from the input field. csrfmiddlewaretoken generated with task:test data
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")
