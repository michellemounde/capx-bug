import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

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
        description = "This is a bug_type with 3 characters"
        bug_type = "tri"
        short_bug_type_bug = Bug(description=description, bug_type=bug_type, status="in testing")
        self.assertEqual(len(bug_type), 3)
        with self.assertRaises(ValidationError):
            short_bug_type_bug.full_clean()

    def test_bug_type_max_length(self):
        """
        bug_type is a maximum length of 50
        """
        description = "This is a bug_type with 51 characters"
        bug_type = "Can you imagine this bug_type is 51 characters len?"
        long_bug_type_bug = Bug(description=description, bug_type=bug_type, status="in testing")
        self.assertEqual(len(bug_type), 51)
        with self.assertRaises(ValidationError):
            long_bug_type_bug.full_clean()

    def test_status_min_length(self):
        """
        status is a minimum length of 4
        """
        description = "This is a status with 3 characters"
        status = "tri"
        short_status_bug = Bug(description=description, bug_type="build", status=status)
        self.assertEqual(len(status), 3)
        with self.assertRaises(ValidationError):
            short_status_bug.full_clean()

    def test_status_max_length(self):
        """
        status is a maximum length of 50
        """
        description = "This is a status with 51 characters"
        status = "Can you imagine this status is 51 characters long??"
        long_status_bug = Bug(description=description, bug_type="build", status=status)
        self.assertEqual(len(status), 51)
        with self.assertRaises(ValidationError):
            long_status_bug.full_clean()


class BugIndexViewTests(TestCase):
    def test_welcome_message(self):
        """
        The welcome message is displayed on the index page
        """
        response = self.client.get(reverse("bug:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the bug index.")


class BugsListViewTests(TestCase):
    def test_no_bugs(self):
        """
        If no bugs exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("bug:bugs"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No bugs are registered.")
        self.assertQuerySetEqual(response.context["bugs_list"], [])

    def test_past_bug(self):
        """
        Bugs with a report_date in the past are displayed on the bugs page.
        """
        description = "This is a bug with a date in the past showing in the bugs list"
        time = timezone.now() + datetime.timedelta(days=-30)
        past_bug = Bug.objects.create(description=description, bug_type="new feature",
                                      status="todo", report_date=time)
        response = self.client.get(reverse("bug:bugs"))
        self.assertQuerySetEqual(response.context["bugs_list"], [past_bug])

    def test_future_bug(self):
        """
        Bugs with a report_date in the future aren't displayed on the bugs page.
        """
        description = "This is a bug with a date in the future not showing in the bugs list"
        time = timezone.now() + datetime.timedelta(days=30)
        Bug.objects.create(description=description, bug_type="new feature", status="todo", report_date=time)
        response = self.client.get(reverse("bug:bugs"))
        self.assertContains(response, "No bugs are registered.")
        self.assertQuerySetEqual(response.context["bugs_list"], [])
