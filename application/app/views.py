from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

def newapp(request):
    return HttpResponse("<h1 style='color: red;'>This is a new app view!</h1>")

def about(request):
    return HttpResponse("<h1>name: nilesh</h1><h2>age: 17</h2> <h3>Hobby: cricket</h3> <p> parul university </p>")