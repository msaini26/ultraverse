from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def map(request):
    return render(request, 'map.html')

def events(request):
    return render(request, 'events.html')

def event(request):
    return render(request, 'event.html')