from django.test import TestCase


from home.models import Project


class ProjectModelTest(TestCase):
    @classmethod
    # def setUpTestData(cls) -> None:
    # return super().setUpTestData()
    def setUpTestData(cls):
        cls.project = Project.objects.create(
            project_id=1,
            title='project test',
            slug='project-test',
            description='project one description',
            image='img/project-7.jpg'
        )

    
    def test_project_id(self):
        id = Project.objects.get(project_id=1)
        id_label = id._meta.get_field('project_id').verbose_name
        self.assertEqual(id_label, 'project id')
    
    def test_project_slug(self):
        _slug = Project.objects.get(slug='project-test')
        slug_label = _slug._meta.get_field('slug').verbose_name
        self.assertEqual(slug_label, 'slug')

    def test_title_length(self):
        title = Project.objects.get(project_id=1)
        max_len = title._meta.get_field('title').max_length
        self.assertEqual(max_len, 100)

    def test_description_length(self):
        description = Project.objects.get(project_id=1)
        max_len = description._meta.get_field('description').max_length
        self.assertEqual(max_len, 200)

    def test_get_absolute_url(self):
        _id = Project.objects.get(slug='project-test')
        self.assertEqual(_id.get_absolute_url(), '/works/project-test/')
