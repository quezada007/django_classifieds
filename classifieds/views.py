from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Classified


def home(request):
    classifieds = Classified.objects.all()
    return render(request, 'home.html', {'classifieds': classifieds})


def classified_detail(request, id):
    try:
        classified = Classified.objects.get(id=id)
    except Classified.DoesNotExist:
        raise Http404('Classified Not Found')
    return render(request, 'classified_detail.html', {'classified': classified})
