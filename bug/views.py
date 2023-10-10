from django.shortcuts import render

from .forms import BugForm


# Create your views here.
def index(request):
    return render(request, "bug/index.html")


def register_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            # TODO - Process data in form.cleaned_data by 1.Save in database
            # TODO - Clear form
            # TODO - Show success message or Redirect to a new url
            return "success"
    else:
        form = BugForm()
    return render(request, "bug/register.html", {"form": form})
