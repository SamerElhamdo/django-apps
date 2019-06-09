from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    """Home view callable, for the home page."""
    return HttpResponse("Hello World!")