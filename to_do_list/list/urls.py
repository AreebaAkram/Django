from django.urls import path
from .import views

urlpatterns = [
    path('task', views.tasks, name='task'),
    path('date', views.dates, name='date'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    ]