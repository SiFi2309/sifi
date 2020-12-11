from django.urls import path
from kba import views

urlpatterns = [
    path('', views.index),
]
