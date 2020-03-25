from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Hood, Post, Bussiness
import cloudinary

class UserManagerTests(TestCase):
    '''Test creating custom user model'''
    def setUp(self) -> None:
        '''Function to prepare before running every testcase'''
        self.test_user = User.objects.create_user(email='test@test.com', password='Test2020')
        self.test_superuser = User.objects.create_superuser('admin@admin.com', 'admin')
        
    def tearDown(self) -> None:
        '''To clean up after running every test case'''
        User.objects.all().delete()
    
    def test_create_user(self):
        '''Test creating of a user'''
        self.assertTrue(self.test_user.is_active)
        self.assertFalse(self.test_user.is_staff)
        self.assertFalse(self.test_user.is_superuser)
        try:
            # Username will be None
            self.assertIsNone(self.test_user.username)
        except AttributeError:
            pass
    
    def test_create_superuser(self):
        '''Test creating of a superuser'''
        self.assertTrue(self.test_user.is_active)
        self.assertTrue(self.test_user.is_staff)
        self.assertTrue(self.test_user.is_superuser)
        try:
            # Username will be None
            self.assertIsNone(self.test_user.username)
        except AttributeError:
            pass

class TestProfileClass(TestCase):
    '''Test class for the Profile model'''
    def setUp(self) -> None:
        '''Prepare before running each testcase'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
        self.test_profile = Profile(username = 'Test', bio = 'This is a test bio', profile_picture='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg', location='Nairobi', user_key=self.test_user)

    def tearDown(self) -> None:
        '''Clean up after running every test case'''
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_isinstance(self):
        '''Test if the profile object is an instance of the Profile class'''
        self.assertTrue(isinstance(self.test_profile, Profile))

    def test_save_profile(self):
        '''Test saving the profile'''
        self.test_profile.save_class()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)

    def test_delete_profile(self):
        '''Test deleting a profile'''
        self.test_profile.save_class()
        self.test_profile.delete_class()
        cloudinary.uploader.destroy(self.test_profile.profile_picture.public_id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile(self):
        '''Test Updating a profile'''
        self.test_profile.save_class()
        self.test_profile.update_class(bio='This is a new test bio')
        profile = Profile.object.get(id = self.test_profile.id)
        self.assertEqual(profile.bio, self.test_profile.bio)

class TestHoodModel(TestCase):
    '''Test Class for the Hood Class'''
    def setUp(self) -> None:
        '''Prepare before running every test case'''

    def test_get_occupants_count(self):
        '''Test getting the total number of occupants in a hood'''
