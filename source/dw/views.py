from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'dw/index.html')


def vessels_index(request):
    vessels = Vessel.objects.all()
    types = VesselType.objects.all()
    context = {'vessels': vessels, 'types': types}
    return render(request, 'dw/vessels/index.html', context)


def by_type(request, type_id):
    vessels = Vessel.objects.filter(type=type_id)
    types = VesselType.objects.all()
    current_type = VesselType.objects.get(pk=type_id)
    context = {'vessels': vessels, 'types': types, 'current_type': current_type}
    return render(request, 'dw/vessels/by_type.html', context)


