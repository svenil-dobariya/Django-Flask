from django.shortcuts import render
from django.http import HttpResponse
from .models import person
# Create your views here.

def cview(request):
    persons = person.objects.all().values()
    data = {
        'persons': persons
    }
    return render(request, 'hi.html', data)