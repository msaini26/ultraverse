from django.shortcuts import render
from .models import *

import logging
logger = logging.getLogger('django')

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

# This is temporary for testing on backend
def developer(request):
    events = Event.objects.order_by('author').all()
    comments = Comment.objects.order_by('author').all()
    
    context = {
        'events': events,
        'comments': comments,
    }

    logger.info('Developer template was rendered.')
    return render(request, 'developer.html', context)