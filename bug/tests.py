import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Bug


# Create your tests here.
class BugModelTests(TestCase):
    def test_was_reported_recently_with_recent_bug(self):
        """
        was_reported_recently() returns True for bugs whose report_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        description = "Testing for was_reported_recently() on recent dates"
        recent_bug = Bug(description=description, bug_type="error", status="todo", report_date=time)
        self.assertIs(recent_bug.was_reported_recently(), True)

    def test_was_reported_recently_with_old_bug(self):
        """
        was_reported_recently() returns False for bugs whose report_date is older than a day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        description = "Testing for was_reported_recently() on old dates"
        old_bug = Bug(description=description, bug_type="error", status="todo", report_date=time)
        self.assertIs(old_bug.was_reported_recently(), False)

    def test_was_reported_recently_with_future_bug(self):
        """
        was_reported_recently() returns False for bugs whose report_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        description = "Testing for was_reported_recently() on future dates"
        future_bug = Bug(description=description, bug_type="error", status="todo", report_date=time)
        self.assertIs(future_bug.was_reported_recently(), False)
