from django.db import models
import datetime
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=400)
    beginning = models.DateTimeField()
    ending = models.DateTimeField()

    def __str__(self):
        return self.title
