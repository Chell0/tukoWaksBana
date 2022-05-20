from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    """Register models here"""
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Project, ProjectAdmin)
