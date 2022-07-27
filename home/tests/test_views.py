from urllib import response
from django.test import TestCase
from django.urls import reverse

from home.models import Project


class ProjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        num_projects = 10

        for project_id in range(num_projects):
            Project.objects.create(project_id=project_id, slug='slug')

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