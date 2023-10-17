from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse

from .forms import BugForm

from .models import Bug


# Create your views here.
def index(request):
    return render(request, "bug/index.html")


def register_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            bug = Bug(**form.cleaned_data)
            bug.save()
            return HttpResponseRedirect(reverse("bug:bugs"))
    else:
        form = BugForm()
    return render(request, "bug/register.html", {"form": form})


def bugs(request):
    bugs = get_list_or_404(Bug)
    return render(request, "bug/bugs.html", {"bugs": bugs})


def detail(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    fields = {field.name: getattr(bug, field.name) for field in bug._meta.get_fields()}
    return render(request, "bug/detail.html", {"bug": bug, "fields": fields})
