from django.shortcuts import render


def addprinter(request):
    return render(request, "adddevice/addprinter.html")
