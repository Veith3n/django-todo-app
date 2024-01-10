from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task
from .enums.urls import TasksUrls
from django.contrib.auth.decorators import login_required
from .utils import log_activity
from .models import ActivityLog
from django.core.exceptions import ValidationError
from .enums.task_actions import TaskAction


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by("created_at")

    return render(request, "tasks/index.html", {"tasks": tasks})


@login_required
def create(request):
    form = TaskForm()
    if request.method == "POST":
        return _handle_form_update(req=request, action=TaskAction.CREATE.value)

    return render(request, "tasks/create.html", {"task_form": form})


@login_required
def update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if task.user == request.user:
            form = TaskForm(instance=task)
            if request.method == "POST":
                return _handle_form_update(req=request, instance=task, action=TaskAction.UPDATE.value)

        return render(request, "tasks/update.html", {"task_edit_form": form})

    except:
        Task.DoesNotExist
    return redirect(TasksUrls.INDEX.value)


@login_required
def delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete() if task.user == request.user else None
        log_activity(request.user, TaskAction.UPDATE.value, f'Task "{task.title}" deleted.')

        return redirect(TasksUrls.INDEX.value)

    except:
        Task.DoesNotExist
    return redirect(TasksUrls.INDEX.value)


@login_required
def activity_log(request):
    valid_sort_fields = ["timestamp", "action_type"]
    sort_param = request.GET.get("sort", "-timestamp")

    if sort_param.strip("-") not in valid_sort_fields:
        sort_param = "-timestamp"

    logs = ActivityLog.objects.filter(user=request.user).order_by(sort_param)

    return render(request, "activity_logs/index.html", {"logs": logs})


def _handle_form_update(req, action, instance=None):
    form = TaskForm(req.POST) if instance is None else TaskForm(req.POST, instance=instance)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = req.user
        task.save()
        log_activity(req.user, action, f'Task "{task.title}" {action}.')

        return redirect(TasksUrls.INDEX.value)
