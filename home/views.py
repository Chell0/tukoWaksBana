from django.shortcuts import render, get_object_or_404
from .models import Project
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET


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

# @require_GET
# @cache_control(max_age=60 * 60 * 24, immutable=True, public=True)
# def favicon(request: HttpRequest) -> HttpRequest:
#     file = (settings.BASE_DIR / 'home' / 'static' / 'favicon.png').open('rb')
#     return FileResponse(file)
