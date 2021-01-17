from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task
from .enums.urls import TasksUrls


def index(request):
    tasks = Task.objects.all().order_by('created_at')

    return render(request, "tasks/index.html", {"tasks": tasks})


def create(request):
    form = TaskForm()
    if request.method == "POST":
        return _handle_form_update(req=request)

    return render(request, "tasks/create.html", {"task_form": form})


def update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        if request.method == "POST":
            return _handle_form_update(req=request, instance=task)

        return render(request, "tasks/update.html", {"task_edit_form": form})

    except:
        Task.DoesNotExist
    return redirect(TasksUrls.INDEX.value)


def delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect(TasksUrls.INDEX.value)

    except:
        Task.DoesNotExist
    return redirect(TasksUrls.INDEX.value)


def _handle_form_update(req, instance=None):
    form = TaskForm(req.POST) if instance is None else TaskForm(req.POST, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(TasksUrls.INDEX.value)
