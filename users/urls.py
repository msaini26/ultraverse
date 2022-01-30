from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_event/', views.create_event, name='create_event'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('map/', views.map, name='map'),
    path('events/', views.events, name='events'),
    path('event/', views.event, name='event'),
    path('spiderman/', views.spiderman, name='spiderman')
    path('superyoga/', views.superyoga, name='superyoga'),
    # This is a temporary backend testpage
    path('developer/', views.developer, name='developer')
]