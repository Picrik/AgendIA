from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtask', views.add_task, name='addtask'),
]