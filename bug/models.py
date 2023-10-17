import datetime

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    description = models.TextField(validators=[MinLengthValidator(25), MaxLengthValidator(200)])
    bug_type = models.CharField(max_length=50, validators=[MinLengthValidator(4)])
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, validators=[MinLengthValidator(4)])

    def __str__(self):
        return self.description

    def was_reported_recently(self):
        now = timezone.now()
        return now >= self.report_date >= now - datetime.timedelta(days=1)
