from django.contrib import admin
from .models import TodoModel  # TOdoModel から TodoModel に修正

# Register your models here.
admin.site.register(TodoModel)
# ここでTodoModelをadminページに登録している
# これでadminページでTodoModelを見れるようになるよ！
