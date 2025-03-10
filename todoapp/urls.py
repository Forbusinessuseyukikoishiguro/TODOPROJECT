from django.contrib import admin
from django.urls import path, include
from.views import TodoList

urlpatterns = [
    path('list/',TodoList.as_view()),
]


#todoapp_urls.py

