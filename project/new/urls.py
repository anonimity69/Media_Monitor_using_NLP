from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('product', views.product, name='product'),
    path("", views.home,name="home"),
    path("model", views.home2,name="method"),
    path("about", views.home3,name="about"),
]


