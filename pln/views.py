from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

# app controllers
def index(request):
    try:
        all_apps = App.objects.all().order_by('name')
        all_applications = Application.objects.all().order_by('name')
        all_formats = Format.objects.all().order_by('name')
        all_functions = Function.objects.all().order_by('name')
        all_prices = Price.objects.all().order_by('name')
        all_supports = Support.objects.all().order_by('name')
    except App.DoesNotExist:
        raise Http404("Application does not exist.")

    return render(request, 'pln/index.html', {'all_apps': all_apps, 'all_applications':all_applications, 'all_functions':all_functions, 'all_formats':all_formats, 'all_prices':all_prices, 'all_supports':all_supports})
