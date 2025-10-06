from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def top(request):
    context = {"name": "あれん"}
    return render(request, "work05/index.html", context)


def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")
