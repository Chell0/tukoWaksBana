from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Project


# Views
def home(request):
    """Get the home page"""
    return render(request, 'home.html')

def approach(request):
    """Get the approach page"""
    return render(request, 'approach.html')

def works(request):
    """Get all projects"""
    projects = Project.objects.all()
    return render(request, 'works.html', { 'projects': projects })

def work_detail(request, project_id):
    """Get a single project using the project id"""
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'work_detail.html', {'project': project})

def services(request):
    """Get the services page"""
    return render(request, 'services.html')

def contact(request):
    """Get the contact page"""
    return render(request, 'contact.html')
