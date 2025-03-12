from django.contrib import admin
from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete , TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),  # ここにカンマが必要
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'), # 'dekete'を'delete'に修正
    path('update/<int:pk>/', TodoDelete.as_view(), name='update')  
]

# todoapp_urls.py