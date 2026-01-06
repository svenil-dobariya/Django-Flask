from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data = [
        {'name': 'Inception', 'genre': 'Sci-Fi'},
        {'name': 'The Dark Knight', 'genre': 'Action'},
        {'name': 'Interstellar', 'genre': 'Sci-Fi'},
        {'name': 'Pulp Fiction', 'genre': 'Crime'},
        {'name': 'The Shawshank Redemption', 'genre': 'Drama'},
        {'name': 'The Godfather', 'genre': 'Crime'},
        {'name': 'Forrest Gump', 'genre': 'Drama'},
        {'name': 'The Matrix', 'genre': 'Sci-Fi'},
    ]
    return render(request, 'index.html', {'movies': data})

def newapp(request):
    return HttpResponse("<h1 style='color: red;'>This is a new app view!</h1>")

def about(request):
    return HttpResponse("<h1 style='color: blue; size: 56px;'>name: nilesh</h1><h2 style='color: green; size: 50px;'>age: Minor</h2> <h3 style='color: purple; size: 48px;'>Hobby: If you know you know....zzzzz</h3> <p style='color: orange; size: 36px;'> parul university(Sadly)</p>")

def home_page(request):
    data = [
        {'name': 'Inception', 'genre': 'Sci-Fi'},
        {'name': 'The Dark Knight', 'genre': 'Action'},
        {'name': 'Interstellar', 'genre': 'Sci-Fi'},
        {'name': 'Pulp Fiction', 'genre': 'Crime'},
        {'name': 'The Shawshank Redemption', 'genre': 'Drama'},
    ]
    return render(request, 'index.html' , {'movies': data})

def contact(request):
    contact = {
        'name' : 'nilesh',
        'age' : 'minor',
        'hobby' : 'If you know you know....zzzzz',
        'university' : 'parul university(Sadly)'
    }
    return render(request, 'contact.html', {'contact': contact})