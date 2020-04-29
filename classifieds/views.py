from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Classified
from .forms import ClassifiedForm


def home(request):
    classifieds = Classified.objects.all().order_by('-submission_date')
    return render(request, 'home.html', {'classifieds': classifieds})


def classified_detail(request, id):
    try:
        classified = Classified.objects.get(id=id)
    except Classified.DoesNotExist:
        raise Http404('Classified Not Found')
    return render(request, 'classified_detail.html', {'classified': classified})


def classified_add(request):
    if request.method == 'POST':
        filled_form = ClassifiedForm(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Thanks for adding a classified ad!'
            filled_form = ClassifiedForm()
        else:
            note = 'Please update the errors and try again'
        return render(request, 'classified_add.html', {'form': filled_form, 'note': note})
    else:
        form = ClassifiedForm()
        return render(request, 'classified_add.html', {'form': form})
