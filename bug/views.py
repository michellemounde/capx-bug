from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

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


class BugsView(generic.ListView):
    template_name = "bug/bugs.html"
    context_object_name = "bugs_list"

    def get_queryset(self) -> QuerySet[Any]:
        """Return all the registered bugs"""
        return Bug.objects.all()


class DetailView(generic.DetailView):
    model = Bug
    template_name = "bug/detail.html"
    context_object_name = "bug"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        bug = context["bug"]
        context["fields"] = {field.name: getattr(bug, field.name) for field in bug._meta.get_fields()}
        return context
