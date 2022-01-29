from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Select

from .models import Event, Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EventForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['author'].disabled = True
    class Meta:
        model = Event
        fields = ['author', 'title', 'description', 'link']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']