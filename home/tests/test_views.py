from urllib import response
from django.test import TestCase
from django.urls import reverse

from home.models import Project


class ProjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:        
       Project.objects.create(project_id=1, title='project test', slug='project-test', description='project one description', image='/media/img/1')   

    def test_view_url_is_at_correct_place(self):
        response = self.client.get('/works/')
        self.assertEqual(response.status_code, 200) 

    def test_view_url_reachable_by_name(self):
        response = self.client.get(reverse('home:works'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home:works'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'works.html')

    def test_list_all_projects(self):
        response = self.client.get(reverse('home:works'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context), 2)