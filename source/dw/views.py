from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    vessels = Vessel.objects.all()
    return render(request, 'dw/index.html', {'vessels': vessels})