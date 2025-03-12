from django.shortcuts import render
# DetailViewではなくDeleteViewを継承する
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import TodoModel
from django.urls import reverse_lazy  # 追加が必要

# Create your views here.
class TodoList (ListView):
    template_name = 'list.html' 
    model = TodoModel  # TOdoModel から TodoModel に修正
    
    
    
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    
    
# 正しい書き方
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ['title', 'memo', 'priority', 'duedate']  # フォームに表示するフィールド
    success_url = reverse_lazy('list')
    
    #success_url = '/'  # 作成成功後のリダイレクト先


class TodoDelete(DeleteView):  # DetailViewではなくDeleteView
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


#todoappのviews.py