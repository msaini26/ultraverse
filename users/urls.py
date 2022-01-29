from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_event/', views.create_event, name='create_event'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('developer/', views.developer, name='developer')
]