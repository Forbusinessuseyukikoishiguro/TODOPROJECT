from django.db import models
from django.utils import timezone

CHOICE =(('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE,
        default='primary'  # デフォルト値を設定
    )
    duedate = models.DateField(default=timezone.now)  # デフォルト値を設定
    
    def __str__(self):
        return self.title