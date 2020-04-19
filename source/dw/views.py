from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from .models import *

# Create your views here.
def index(request):
    return render(request, 'dw/index.html')


def other_page(request, page):
    try:
        template = get_template('dw/{}.html'.format(page))
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class MainLoginView(LoginView):
    template_name = 'dw/login.html'


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


