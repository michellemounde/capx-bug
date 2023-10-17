import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Bug


# Create your tests here.
class BugModelTests(TestCase):
    def test_was_reported_recently_with_future_bug(self):
        """
        was_reported_recently() returns False for questions whose report_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        description = "Testing for was_reported_recently() on future dates"
        future_bug = Bug(description=description, bug_type="error", status="todo", report_date=time)
        self.assertIs(future_bug.was_reported_recently(), False)
