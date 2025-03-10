from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TodoModel
from .models import TodoModel  # モデル名が正しくインポートされていることを確認
# Create your views here.
class TodoList (ListView):
    template_name = 'list.html' 
    model = TodoModel  # TOdoModel から TodoModel に修正
    
    
#todoappのviews.py