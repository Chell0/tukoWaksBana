from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    '''Model representing a project'''
    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField()
    images = models.FilePathField(path="/img")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("work_detail", kwargs={"pk": self.pk})