from django.test import TestCase
from django.contrib.auth import get_user_model

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



# Create your tests here.
