from django.db import models
from datetime import date


# Create your models here.
class Bug(models.Model):
    description = models.TextField()
    bug_type = models.CharField(max_length=200)
    report_date = models.DateField(default=date.today)
    status = models.CharField(max_length=200)
