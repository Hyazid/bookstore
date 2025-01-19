from django.test import TestCase
from django.urls import reverse,resolve
from django.contrib.auth import get_user_model
from .views import SignupPageView
from .forms import CustomUserCreationForm

class CustomUserTest(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='test123'
            )
        self.assertEqual(user.username,'testuser')
        self.assertEqual(user.email,'testuser@test.com')
        self.assertTrue(user.check_password('test123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='adminuser',
            email='adminuser@test.com',
            password='test123'
            )
        self.assertEqual(admin_user.username,'adminuser')
        self.assertEqual(admin_user.email,'adminuser@test.com')
        self.assertTrue(admin_user.check_password('test123'))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url= reverse('signup')
        self.response= self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'registration/signup.html')
        self.assertContains(self.response,'Sign Up')
        self.assertNotContains(self.response,'hi i should not be in this page')
    def test_signup_view(self):
        view=resolve('/accounts/signup/')
        self.assertEqual(view.func.view_class,SignupPageView)
    def test_signup_form(self):
        form=self.response.context.get('form')
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretiken')
# Create your tests here.
