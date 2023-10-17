import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    description = models.TextField()
    bug_type = models.CharField(max_length=50)
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    def was_reported_recently(self):
        return self.report_date >= timezone.now() - datetime.timedelta(days=1)
