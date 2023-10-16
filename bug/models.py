import datetime

from django.db import models
from django.utils import timezone


class BugManager(models.Manager):
    def create_bug(self, description, bug_type, status):
        bug = self.create(description=description, bug_type=bug_type, status=status)
        return bug


# Create your models here.
class Bug(models.Model):
    description = models.TextField()
    bug_type = models.CharField(max_length=50)
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)

    objects = BugManager()

    def __str__(self):
        return self.description

    def was_reported_recently(self):
        return self.report_date >= timezone.now() - datetime.timedelta(days=1)
