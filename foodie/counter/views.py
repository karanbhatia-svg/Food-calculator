from django.shortcuts import render

# Create your views here.
def home(request):
    api = "string"
    return render(request, "counter/home.html", {'api': api})