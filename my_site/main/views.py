from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "main/index.html")

def house(request):
    return render(request, "main/house.html")

def building(request):
    return render(request, "main/building.html")

def about(request):
    return render(request, "main/about.html")
