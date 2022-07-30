from django.shortcuts import render, get_object_or_404
from .models import Project
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET


# Views
def home(request):
    """Get selected projects on the home page"""
    projects = Project.objects.all()[:4]
    return render(request, 'home.html', {'projects': projects})


def approach(request):
    """Get the approach page"""
    return render(request, 'approach.html')


def works(request):
    """Get all projects"""
    projects = Project.objects.all()
    return render(request, 'works.html', {'projects': projects})


def work_detail(request, slug):
    """Get a single project using the project id"""
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'work_detail.html', {'project': project})


def services(request):
    """Get the services page"""
    return render(request, 'services.html')


def contact(request):
    """Get the contact page"""
    return render(request, 'contact.html')


def page_not_found(request):
    """Get the 404 page"""
    return render(request, '404.html', status=404)


def server_error(request):
    """Get the 500 page"""
    return render(request, '500.html', status=500)
