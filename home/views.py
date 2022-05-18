from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    """Get the home page"""
    return render(request, 'home.html')

def approach(request):
    """Get the approach page"""
    return render(request, 'approach.html')

def works(request):
    """Get all projects"""
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, 'works.html', context)

def work_detail(request, project_id):
    """Get a single project using the project id"""
    project = Project.objects.get(pk=project_id)
    context = { 'project': project }
    return render(request, 'work_detail.html', context)

def services(request):
    """Get the services page"""
    return render(request, 'services.html')

def contact(request):
    """Get the contact page"""
    return render(request, 'contact.html')
