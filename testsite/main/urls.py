from django.urls import path
from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("process/", views.get_processes, name="getProcess")
]