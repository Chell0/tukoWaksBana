from django.db import models
from django.urls import reverse


# Project Model
class Project(models.Model):
    '''Model representing a project'''
    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, null=False)
    description = models.TextField(max_length=200)
    images = models.ImageField(upload_to="img")

    class Meta:
        verbose_name = 'project'
        ordering = ['-project_id']

    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse('home:work_detail', kwargs={'slug': self.slug})
