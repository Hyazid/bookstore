from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_page_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_homepage_template(self): # new
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    def test_aboutpage_contains_correct_html(self):
        self.assertIn('About', self.response.content.decode())
        self.assertNotIn('Hi, I should not be in this page', self.response.content.decode())
    def test_aboutpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response,'hi there')
    def test_aboutpage_url_resolver_aboutpageview(self):
        view = reverse('about')
        self.assertEqual(view, '/about')
        self.assertEqual(resolve(view).func.view_class, AboutPageView)
# Create your tests here.
