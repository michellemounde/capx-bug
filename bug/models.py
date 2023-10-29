import datetime

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    FEATURE = "FEAT"
    ERROR = "ERR"
    FUNCTIONAL = "FUNC"
    LOGICAL = "LOGIC"
    WORKFLOW = "FLOW"
    USABILITY = "UIUX"
    SECURITY = "SEC"
    PERFORMANCE = "PERF"
    COMPATIBILITY = "COMP"
    UNIT = "UNIT"
    SYSTEM = "SYS"
    OUTOFBOUND = "OUT"
    BUG_TYPE_CHOICES = [
        (FEATURE, "New Feature"),
        (ERROR, "Error"),
        (FUNCTIONAL, "Functional"),
        (LOGICAL, "Logical"),
        (WORKFLOW, "Workflow"),
        (USABILITY, "Usability"),
        (SECURITY, "Security"),
        (PERFORMANCE, "Performance"),
        (COMPATIBILITY, "Compatibility"),
        (UNIT, "Unit Level"),
        (SYSTEM, "System Level"),
        (OUTOFBOUND, "Out of Bound"),
    ]

    TODO = "TODO"
    PLANNING = "PLAN"
    DESIGNING = "DESIGN"
    PROTOTYPING = "PROTO"
    WIP = "WIP"
    TESTING = "TEST"
    RNA = "RNA"
    STAGING = "STAGE"
    MERGING = "MERGE"
    STATUS_CHOICES = [
        (TODO, "To-Do"),
        (PLANNING, "Planning"),
        (DESIGNING, "Designing"),
        (PROTOTYPING, "Prototyping"),
        (WIP, "Work in Progress"),
        (TESTING, "Testing"),
        (RNA, "Review & Approval"),
        (STAGING, "Staging"),
        (MERGING, "Merging"),
    ]
    description = models.TextField(validators=[MinLengthValidator(25), MaxLengthValidator(200)])
    bug_type = models.CharField(max_length=5, choices=BUG_TYPE_CHOICES)
    report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)

    def __str__(self):
        return self.description

    def was_reported_recently(self):
        now = timezone.now()
        return now >= self.report_date >= now - datetime.timedelta(days=1)
