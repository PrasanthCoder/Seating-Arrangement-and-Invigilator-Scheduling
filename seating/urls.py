from django.urls import path
from . import views

urlpatterns = [
    path('input',views.input, name='input'),
    path('',views.home, name='home')
]