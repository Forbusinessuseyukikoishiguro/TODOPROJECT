from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todoapp.urls")),
    # 空欄何もURL記載ないなら、todoapp呼び出す
]
