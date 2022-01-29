from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('map/', views.map, name='map'),
    path('events/', views.events, name='events'),
    path('event/', views.event, name='event'),
    path('superyoga/', views.superyoga, name='superyoga')
]