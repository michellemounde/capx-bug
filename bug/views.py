from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the bug index.")


def register_bug(request):
    return HttpResponse("TODO - Add form here to register bugs!")
