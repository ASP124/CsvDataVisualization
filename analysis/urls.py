from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<str:filename>/', views.results, name='results'),
     path('visualizations/<str:filename>/', views.visualizations, name='visualizations'),
]