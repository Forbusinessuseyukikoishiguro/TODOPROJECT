from django.db import models


# Create your models here.
class TOdoModer(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
