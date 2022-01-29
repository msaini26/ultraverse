from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

import logging
logger = logging.getLogger('django')

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    # if request.user.is_authenticated:
    #     logger.info('Login template was not rendered. User was redirected to home.')
    #     return redirect('home')
    # else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                logger.info('Login successful. Redirecting to dashboard.')
                return redirect('dashboard')
            else: 
                messages.info(request, 'username or password is incorrect')
        
        logger.info('Login template was rendered.')
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