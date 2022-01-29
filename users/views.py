from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import UserRegisterForm, EventForm, CommentForm

import logging
logger = logging.getLogger('django')

# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_register(request):
    if request.user.is_authenticated:
        logger.info('Register template was not rendered. User was redirected to home.')
        return redirect('home')
    else:
        form = UserRegisterForm()
    
        if request.method == 'POST':
            # Django default UserCreationForm handles hashing and making sure user doesn't already exist
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, username + f' has been created! You are now able to log in.')
                logger.info('New user data saved.')
                logger.info('Redirecting to login page.')
                return redirect('login')
        else: 
            form = UserRegisterForm()
        
        context = {'form':form}
        
        logger.info('Register template was rendered.')
        return render(request, 'register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        logger.info('Login template was not rendered. User was redirected to home.')
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # TODO: Fix redirect once we have an established page to redirect user upon login
                logger.info('Login successful. Redirecting to home.')
                return redirect('home')
            else: 
                messages.info(request, 'username or password is incorrect')
        
        logger.info('Login template was rendered.')
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    logger.info('User has been logged out and redirected to login.')
    return redirect('login')

def create_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        logger.info('Test Print: ', request.POST)
        if form.is_valid:
            form.save()
            logger.info('Event data was posted.')
            logger.info('Redirecting to home.')
            return redirect('home')
    
    context = {'form':form}
    
    logger.info('Event form template was rendered.')
    return render(request, 'event_form.html', context)

def create_comment(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        logger.info('Test Print: ', request.POST)
        if form.is_valid:
            form.save()
            logger.info('Event data was posted.')
            logger.info('Redirecting to home.')
            return redirect('home')
    
    context = {'form':form}
    
    logger.info('Event form template was rendered.')
    return render(request, 'event_form.html', context)

# This is temporary for testing on backend
def developer(request):
    events = Event.objects.order_by('date_posted').all()
    comments = Comment.objects.order_by('date_posted').all()
    
    context = {
        'events': events,
        'comments': comments,
    }

    logger.info('Developer template was rendered.')
    return render(request, 'developer.html', context)