from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newapp/', views.newapp, name='newapp'),
    path('about/', views.about, name='about'),
    path('home/', views.home_page, name='home_page'),
    path('contact/', views.contact, name='contact'),
]