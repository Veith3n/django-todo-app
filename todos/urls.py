from django.urls import path
from . import views
from .enums.urls import TasksUrls

urlpatterns = [
    path("", views.index, name=TasksUrls.INDEX.value),
    path("tasks", views.create, name=TasksUrls.CREATE.value),
    path("tasks/<int:pk>/", views.update, name=TasksUrls.UPDATE.value),
    path("tasks/<int:pk>/del", views.delete, name=TasksUrls.DELETE.value),
    path("activity-log/", views.activity_log, name="activity_logs/activity_log"),
]
