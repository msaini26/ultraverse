from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.RESTRICT)
    title = models.CharField(max_length=100, null=False, blank=False, default='')
    description = models.CharField(max_length=350, null=False, blank=False, default='')
    link = models.CharField(max_length=300, null=False, blank=False, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, null=True, default='', blank=False, on_delete=models.RESTRICT)
    comment = models.TextField(max_length=150, null=False, blank=False, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.comment