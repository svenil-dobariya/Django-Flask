from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

def newapp(request):
    return HttpResponse("<h1 style='color: red;'>This is a new app view!</h1>")

def about(request):
    return HttpResponse("<h1 style='color: blue; size: 56px;'>name: nilesh</h1><h2 style='color: green; size: 50px;'>age: Minor</h2> <h3 style='color: purple; size: 48px;'>Hobby: If you know you know....zzzzz</h3> <p style='color: orange; size: 36px;'> parul university(Sadly)</p>")