from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        "title": "Главная страница",
        "values": ["Some", "Hello", "123"],
    }
    return render(request, "main/index.html", context=data)


def addprinter(request):
    return render(request, "main/addprinter.html")


def about(request):
    return render(request, "main/about.html")
