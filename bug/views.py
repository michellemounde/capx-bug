from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
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
            bug = Bug.objects.create_bug(**form.cleaned_data)
            bug.save()
            return "success"
    else:
        form = BugForm()
    return render(request, "bug/register.html", {"form": form})
