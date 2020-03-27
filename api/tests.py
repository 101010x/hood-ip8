from django.test import TestCase
from .models import Profile, Hood, Post, Bussiness, User
import cloudinary

class TestAbstractUser(TestCase):
    '''Test class to test the abstract test user extension'''
    def setUp(self):
        '''To prepare before running every testcase'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
    
    def tearDown(self):
        '''To clean up after running every test case'''
        User.objects.all().delete()

    def test_default_user_admin_status(self):
        '''To test that the default user admin status is False'''
        self.assertEqual(self.test_user.is_admin_status, False)

    def test_change_default_user_admin_status(self):
        '''Test to update the default user admin status'''
        self.test_user.is_admin_status = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_admin_status, True)


class TestProfileClass(TestCase):
    '''Test class for the Profile model'''
    def setUp(self) -> None:
        '''Prepare before running each testcase'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
        self.test_profile = Profile(bio = 'This is a test bio', profile_picture='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg', location='Nairobi', user=self.test_user)
        self.test_profile.save_class()

    def tearDown(self) -> None:
        '''Clean up after running every test case'''
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_isinstance(self):
        '''Test if the profile object is an instance of the Profile class'''
        self.assertTrue(isinstance(self.test_profile, Profile))

    def test_save_profile(self):
        '''Test saving the profile'''
        self.new_user = User(username='randomn',email='random@random.com', password='test2020')
        self.new_user.save()
        self.new_profile = Profile(bio = 'This is a new test bio', profile_picture='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg', location='Nairobi', user=self.new_user)
        self.new_profile.save_class()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 2)

    def test_delete_profile(self):
        '''Test deleting a profile'''
        self.test_profile.delete_class()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile(self):
        '''Test Updating a profile'''
        self.test_profile.update_class(bio='This is a new test bio')
        profile = Profile.objects.get(id = self.test_profile.id)
        self.assertEqual(profile.bio, self.test_profile.bio)

    def test_update_profile_hood(self):
        '''Test updating a users hood'''
        self.test_hood = Hood(hood_name = 'TestHood', location='Nairobi')
        self.test_hood.save_class()
        self.test_profile.hood = self.test_hood
        self.test_profile.save_class()
        self.assertEqual(self.test_profile.hood, self.test_hood)

class TestHoodModel(TestCase):
    '''Test Class for the Hood Class'''
    def setUp(self) -> None:
        '''Prepare before running every test case'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
        self.test_hood = Hood(hood_name = 'TestHood', location='Nairobi')
        self.test_hood.save_class()

    def tearDown(self):
        '''To clean up after running every test case'''
        User.objects.all().delete()
        Profile.objects.all().delete()
        Hood.objects.all().delete()

    def test_isinstance(self):
        '''Test if the hood is an instance of the Hood class'''
        self.assertTrue(isinstance(self.test_hood, Hood))

    def test_save_hood(self):
        '''To test saving a hood'''
        self.new_hood = Hood(hood_name = 'NewHood', location='Nairobi')
        self.new_hood.save_class()
        hoods = Hood.objects.all().count()
        self.assertTrue(hoods == 2)

    def test_delete_hood(self):
        '''Testing deleting a hood'''
        self.test_hood.delete_class()
        hoods = Hood.objects.all().count()
        self.assertTrue(hoods == 0)

    def test_update_hood(self):
        '''Test Updating a hood'''
        self.test_hood.update_class(location='Kisumu')
        hood = Hood.objects.get(id = self.test_hood.id)
        self.assertEqual(hood.location, self.test_hood.location)

    def test_get_and_update_occupants_count(self):
        '''Test getting the total number of occupants in a hood'''
        hood = Hood.objects.get(id = self.test_hood.id)
        self.assertEqual(hood.occupants_count,0)
        self.test_hood.update_class(occupants_count = 2)
        hood = Hood.objects.get(id = self.test_hood.id)
        self.assertEqual(hood.occupants_count,2)

    def test_hood_has_no_admin(self):
        '''Testing that a hood has no admin at first'''
        self.assertTrue(self.test_hood.admin == None)

    def test_update_hood_admin(self):
        '''Test that a hood can be assigned an admin'''
        self.new_user = User(username='randomn',email='random@random.com', password='test2020')
        self.new_user.is_admin_status = True
        self.new_user.save()
        self.test_hood.update_hood_admin(self.new_user)
        self.assertTrue(self.test_hood.admin == self.new_user)
        self.assertRaises(ValueError, self.test_hood.update_hood_admin, self.test_user)

class TestPost(TestCase):
    '''Test class to test the Post class'''
    def setUp(self):
        '''To prepare before running every test case'''
        self.test_hood = Hood(hood_name = 'TestHood', location='Nairobi')
        self.test_hood.save_class()
        self.new_user = User(username='randomn',email='random@random.com', password='test2020')
        self.new_user.save()
        self.test_post = Post(post_title='Test Post', post_content='This is a test post', post_image='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg', user=self.new_user, hood=self.test_hood)
        self.test_post.save_class()

    def tearDown(self):
        '''To clean up after running every test case'''
        Hood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_isinstance(self):
        '''To test that  post is an instance of the Post class'''
        self.assertTrue(isinstance(self.test_post, Post))
    
    def test_save_post(self):
        '''To test saving of a post'''
        posts = Post.objects.all().count()
        self.assertTrue(posts == 1)
    
    def test_delete_post(self):
        '''To test deleting of a post'''
        self.test_post.delete_class()
        posts = Post.objects.all().count()
        self.assertTrue(posts == 0)
    
    def test_update_post(self):
        '''To test updating of a post'''
        self.test_post.update_class(post_title = 'New test Post')
        self.assertEqual(self.test_post.post_title, 'New test Post')


class TestBussiness(TestCase):
    '''Test class to test the Bussiness class'''
    def setUp(self):
        '''To prepare before running every test case'''
        self.test_hood = Hood(hood_name = 'TestHood', location='Nairobi')
        self.test_hood.save_class()
        self.test_biz = Bussiness(name='Test Biz', email='biz@biz.com', description='This is a test Bussiness', hood=self.test_hood)
        self.test_biz.save_class()

    def tearDown(self):
        '''To clean up after running every test case'''
        Hood.objects.all().delete()
        Bussiness.objects.all().delete()
    
    def test_isinstance(self):
        '''Test that bussiness is an instance of the Bussiness Class'''
        self.assertTrue(isinstance(self.test_biz, Bussiness))

    def test_save_bussiness(self):
        '''To test saving of a bussiness'''
        bizs = Bussiness.objects.all().count()
        self.assertTrue(bizs == 1)
    
    def test_delete_bussiness(self):
        '''To test deleting of a bussiness'''
        self.test_biz.delete_class()
        bizs = Bussiness.objects.all().count()
        self.assertTrue(bizs == 0)
    
    def test_update_bussiness(self):
        '''To test updating of a bussiness'''
        self.test_biz.update_class(name='New Test Biz')
        biz = Bussiness.objects.get(id = self.test_biz.id)
        self.assertEqual(biz.name, self.test_biz.name)