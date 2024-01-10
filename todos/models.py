from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=350)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=10)  # create, update, delete, etc.
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
