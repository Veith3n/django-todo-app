from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks", views.create, name="create_task"),
    path("tasks/<int:pk>/", views.update, name="update_task"),
    path("tasks/<int:pk>/del", views.delete, name="delete_task"),
]
