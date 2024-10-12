from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  # url path for predict view
  path('predict/',views.predict,name='predict'),
]
