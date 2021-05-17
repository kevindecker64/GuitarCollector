from django.shortcuts import render
from .models import Guitar

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})