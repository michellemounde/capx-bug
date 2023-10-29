from django import forms
from bug.models import Bug


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["description", "bug_type", "report_date", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"] = forms.CharField(widget=forms.Textarea)
        self.fields["bug_type"] = forms.ChoiceField(choices=Bug.BUG_TYPE_CHOICES)
        self.fields["status"] = forms.ChoiceField(choices=Bug.STATUS_CHOICES)
        self.fields["report_date"] = forms.SplitDateTimeField(
                                        widget=forms.SplitDateTimeWidget
                                        (date_attrs={"type": "date"}, time_attrs={"type": "time"}))
