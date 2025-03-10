from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import TodoModel  # モデル名が正しくインポートされていることを確認

# Create your views here.
class TodoList (ListView):
    template_name = 'list.html' 
    model = TodoModel  # TOdoModel から TodoModel に修正
    
    
    
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    
#todoappのviews.py