from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

# Create your models here.
