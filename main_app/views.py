from django.shortcuts import render
from django.http import HttpResponse

class Guitar:
    def __init__(self, make, model, year, description):
        self.make = make
        self.model = model
        self.year = year
        self.description = description

guitars = [
    Guitar('Gibson', 'Ripper', 1981, 'Smooth as butter'),
    Guitar('Fender', 'P-Bass', 2013, 'Phat AF'),
    Guitar('Warwick', 'Corvette', 2006, 'Fretless'),
]

def home(request):
    return HttpResponse('<h1>Hello, get some guitboxes</h1>')
    
def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', {'guitars': guitars})