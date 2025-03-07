from django.contrib import admin
from .models import TOdoModel

# Register your models here.
admin.site.register(TOdoModel)
# ここでTodoModelをadminページに登録している
# これでadminページでTodoModelを見れるようになるよ！
