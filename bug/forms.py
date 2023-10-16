from django import forms


class BugForm(forms.Form):
    description = forms.CharField(min_length=25, max_length=200, widget=forms.Textarea)
    bug_type = forms.CharField(min_length=4, max_length=50)
    status = forms.CharField(min_length=4, max_length=50)
