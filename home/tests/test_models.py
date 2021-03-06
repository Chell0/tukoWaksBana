from audioop import reverse
from django.test import TestCase
from home.models import Project

      
class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
       # return super().setUpTestData()
       Project.objects.create(project_id=1, title='project one', description='project one description')

    
    def test_project_id(self):
        id = Project.objects.get(project_id=1)
        id_label = id._meta.get_field('project_id').verbose_name
        self.assertEqual(id_label, 'project id')

    def test_title_length(self):
        title = Project.objects.get(project_id=1)
        max_len = title._meta.get_field('title').max_length
        self.assertEqual(max_len, 100)

    def test_description_length(self):
        description = Project.objects.get(project_id=1)
        max_len = description._meta.get_field('description').max_length
        self.assertEqual(max_len, 200)

    def test_get_absolute_url(self):
        _id = Project.objects.get(project_id=1)
        self.assertEqual(_id.get_absolute_url(), '/works/1/')
