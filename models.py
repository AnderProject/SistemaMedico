from contextlib import nullcontext
from distutils.command.upload import upload
from django.db import models
# Create your models here.


# Create your models here.
class Task(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.subject