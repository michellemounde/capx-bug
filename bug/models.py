from django.db import models
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    description = models.TextField()
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200)
