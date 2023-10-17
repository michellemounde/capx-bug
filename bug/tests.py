import datetime

from django.core.exceptions import ValidationError
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

    def test_description_min_length(self):
        """
        description is a minimum length of 25
        """
        description = "A sentence with 24 chars"
        short_desc_bug = Bug(description=description, bug_type="build", status="in testing")
        self.assertEqual(len(description), 24)
        with self.assertRaises(ValidationError):
            short_desc_bug.full_clean()

    def test_description_max_length(self):
        """
        description is a maximum length of 200
        """
        description = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                       "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                       "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut al.")
        long_desc_bug = Bug(description=description, bug_type="build", status="in testing")
        self.assertEqual(len(description), 201)
        with self.assertRaises(ValidationError):
            long_desc_bug.full_clean()

    def test_bug_type_min_length(self):
        """
        bug_type is a minimum length of 4
        """
        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        bug_type = "etc"
        short_bug_type_bug = Bug(description=description, bug_type=bug_type, status="in testing")
        self.assertEqual(len(bug_type), 3)
        with self.assertRaises(ValidationError):
            short_bug_type_bug.full_clean()

    def test_bug_type_max_length(self):
        """
        bug_type is a maximum length of 50
        """
        description = "The quick brown fox jumps over the lazy dog"
        bug_type = "Lorem ipsum dolor sit amet, consectetur adipiscing."
        long_bug_type_bug = Bug(description=description, bug_type=bug_type, status="in testing")
        self.assertEqual(len(bug_type), 51)
        with self.assertRaises(ValidationError):
            long_bug_type_bug.full_clean()

    def test_status_min_length(self):
        """
        status is a minimum length of 4
        """
        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        status = "etc"
        short_status_bug = Bug(description=description, bug_type="build", status=status)
        self.assertEqual(len(status), 3)
        with self.assertRaises(ValidationError):
            short_status_bug.full_clean()

    def test_status_max_length(self):
        """
        status is a maximum length of 50
        """
        description = "The quick brown fox jumps over the lazy dog"
        status = "Lorem ipsum dolor sit amet, consectetur adipiscing."
        long_status_bug = Bug(description=description, bug_type="build", status=status)
        self.assertEqual(len(status), 51)
        with self.assertRaises(ValidationError):
            long_status_bug.full_clean()
