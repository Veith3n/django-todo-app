from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task
from .enums.urls import TasksUrls
from django.contrib.auth.decorators import login_required
from .utils import log_activity


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by("created_at")

    return render(request, "tasks/index.html", {"tasks": tasks})


@login_required
def create(request):
    form = TaskForm()
    if request.method == "POST":
        return _handle_form_update(req=request, action="create")

    return render(request, "tasks/create.html", {"task_form": form})


@login_required
def update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if task.user == request.user:
            form = TaskForm(instance=task)
            if request.method == "POST":
                return _handle_form_update(req=request, instance=task, action="update")

        return render(request, "tasks/update.html", {"task_edit_form": form})

    except:
        Task.DoesNotExist
    return redirect(TasksUrls.INDEX.value)


@login_required
def delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete() if task.user == request.user else None
        log_activity(request.user, "delete", f'Task "{task.title}" deleted.')

        return redirect(TasksUrls.INDEX.value)

    except:
        Task.DoesNotExist
    return redirect(TasksUrls.INDEX.value)


def _handle_form_update(req, action, instance=None):
    form = TaskForm(req.POST) if instance is None else TaskForm(req.POST, instance=instance)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = req.user
        task.save()
        log_activity(req.user, action, f'Task "{task.title}" {action}.')

        return redirect(TasksUrls.INDEX.value)
