from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class CrudMethods:
    '''Mixin class for shared classmethods'''
    def save_class(self):
        '''Function to save class to database'''
        self.save()

    def delete_class(self):
        '''Function to delete class from database'''
        self.delete()

    def update_class(self, **kwargs):
        '''Function to update the class in database'''
        for key,value in kwargs.items():
            setattr(self,key,value)
            self.save()

class Profile(models.Model, CrudMethods):
    '''Model table fot the user profile'''
    username = models.CharField(max_length=40)
    bio = models.TextField()
    profile_picture = CloudinaryField('avatar')
    location = models.CharField(max_length=60)
    user_key = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')

class Hood(models.Model, CrudMethods):
    '''Model table for the neighbourhood that a user is assigned'''
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(default=0)
    admin_key = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hoodadmin')

class Post(models.Model, CrudMethods):
    '''Model table for posts that are created by the user'''
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_image = CloudinaryField('image')
    pub_date = models.DateField(auto_now_add=True)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userpost')
    hood_key = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hoodposts')

class Bussiness(models.Model, CrudMethods):
    '''Model Table for the bussinesses/Facilities'''
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    hood_key = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hoodbussinesses')

