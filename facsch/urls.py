from django.urls import path
from . import views

urlpatterns = [
    path('',views.facsch, name='facsch'),
    path('input/',views.input, name='input'),
    path('faclogin/', views.faclogin, name='faclogin'),
    path('facdash/',views.facdash, name='facdash'),
    path('adminlogin/',views.adminlogin, name='adminlogin'),
    path('admindash/', views.admindash, name='admindash')
]