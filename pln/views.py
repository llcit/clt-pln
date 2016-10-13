from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# app controllers
def apps(request):
    try:
        apps = App.objects.all().order_by('name')
        applications = Application.objects.all().order_by('name')
        formats = Format.objects.all().order_by('name')
        functions = Function.objects.all().order_by('name')
        price = Price.objects.all().order_by('name')
        support = Support.objects.all().order_by('name')
    except App.DoesNotExist:
        raise Http404("Application does not exist.")

    return render(request, 'pln/apps.html', {'apps': apps, 'applications':applications, 'functions':functions, 'formats':formats, 'price':price, 'support':support})

def app(request, item_id):
    item = get_object_or_404(App, id=item_id)
    return render(request, 'pln/app.html', {'app': item})

def app_new(request):
    if not request.user.is_authenticated():
        return redirect('/admin')

    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.save()
            return redirect('pln.views.app',item_id=app.id)
    else:
        form = AppForm()
    return render(request, 'pln/app_new.html',{'form': form})

def app_edit(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    app = get_object_or_404(App, id=item_id)
    if request.method == "POST":
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save(commit=False)
            app.save()
            return redirect('pln.views.app', item_id=app.id)
    else:
        form = AppForm(instance=app)
    return render(request, 'pln/app_edit.html',{'form': form})

def app_delete(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    app = get_object_or_404(App, id=item_id)
    app.delete()

    return redirect('/pln')

# application controlers
def applications(request):
    try:
        lists = Application.objects.all()
    except Application.DoesNotExist:
        raise Http404("Application dose not exist.")
    return render(request, 'pln/applications.html', {'lists': lists})


def application(request, item_id):
    item = get_object_or_404(Application, id=item_id)
    return render(request, 'pln/application.html', {'item': item})

def application_new(request):
    if not request.user.is_authenticated():
        return redirect('/admin')

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applications.save()
            return redirect('pln.views.application',item_id=application.id)
    else:
        form = ApplicationForm()
    return render(request, 'pln/application_new.html',{'form': form})

def application_edit(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    application = get_object_or_404(Application, id=item_id)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            return redirect('pln.views.application', item_id=application.id)
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'pln/application_edit.html',{'form': form})

def application_delete(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    application = get_object_or_404(App, id=item_id)
    application.delete()

    return redirect('/pln/applications')

# format controllers
def formats(request):
    try:
        formats = Format.objects.all()
    except Format.DoesNotExist:
        raise Http404("Format does not exist.")
    return render(request, 'pln/formats.html', {'formats': formats})

def format(request, item_id):
    item = get_object_or_404(Format, id=item_id)
    return render(request, 'pln/format.html', {'item': item})

def format_new(request):
    if not request.user.is_authenticated():
        return redirect('/admin')

    if request.method == "POST":
        form = FormatForm(request.POST)
        if form.is_valid():
            format = form.save(commit=False)
            format.save()
            return redirect('pln.views.format',item_id=format.id)
    else:
        form = FormatForm()
    return render(request, 'pln/format_new.html',{'form': form})

def format_edit(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    format = get_object_or_404(Format, id=item_id)
    if request.method == "POST":
        form = FormatForm(request.POST, instance=format)
        if form.is_valid():
            format = form.save(commit=False)
            format.save()
            return redirect('pln.views.format', item_id=format.id)
    else:
        form = FormatForm(instance=format)
    return render(request, 'pln/format_edit.html',{'form': form})

def format_delete(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    format = get_object_or_404(Format, id=item_id)
    format.delete()

    return redirect('/pln/formats')

# function controllers
def functions(request):
    try:
        lists = Function.objects.all()
    except Function.DoesNotExist:
        raise Http404("Function does not exist.")
    return render(request, 'pln/functions.html', {'lists': lists})

def function(request, item_id):
    item = get_object_or_404(Function, id=item_id)
    return render(request, 'pln/function.html', {'item': item})

def function_new(request):
    if not request.user.is_authenticated():
        return redirect('/admin')

    if request.method == "POST":
        form = FunctionForm(request.POST)
        if form.is_valid():
            function = form.save(commit=False)
            function.save()
            return redirect('pln.views.function',item_id=function.id)
    else:
        form = FunctionForm()
    return render(request, 'pln/function_new.html',{'form': form})

def function_edit(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    function = get_object_or_404(Function, id=item_id)
    if request.method == "POST":
        form = FunctionForm(request.POST, instance=function)
        if form.is_valid():
            function = form.save(commit=False)
            function.save()
            return redirect('pln.views.function', item_id=function.id)
    else:
        form = FormatForm(instance=function)
    return render(request, 'pln/function_edit.html',{'form': form})

def function_delete(request, item_id):
    if not request.user.is_authenticated():
        return redirect('/admin')

    function = get_object_or_404(App, id=item_id)
    function.delete()

    return redirect('/pln/functions')
