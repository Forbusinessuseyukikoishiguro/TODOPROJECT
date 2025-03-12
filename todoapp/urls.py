from django.contrib import admin
from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),  # 末尾にスラッシュを追加
    path('create/', TodoCreate.as_view(), name='create')
]

# todoapp_urls.py