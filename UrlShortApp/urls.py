from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('short', views.result, name='result')
    
]