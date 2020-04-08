from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    vessels = Vessel.objects.all()
    return render(request, 'dw/index.html', {'vessels': vessels})


def by_vesselType(request, type_id):
    vessels = Vessel.objects.filter(type=type_id)
    types = VesselType.objects.all()
    current_type = VesselType.objects.get(pk=type_id)
    context = {'vessels': vessels, 'types': types, 'current_type': current_type}
    return render(request, 'dw/by_vesselType.html', context)