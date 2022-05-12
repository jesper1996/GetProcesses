from django.urls import path
from . import views

urlpatterns = [
    path('refresh/', views.refreshData),
    path('get/', views.getData),
    path('', views.getData)
]