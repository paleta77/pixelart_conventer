import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password_hash = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Image(models.Model):
    block_size = models.IntegerField()
    colors_number = models.IntegerField()
    path = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.path} ({self.creator})"

    def is_recent(self):
        return self.created > timezone.now() - datetime.timedelta(days=1)
