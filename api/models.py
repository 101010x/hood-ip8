from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

User = settings.AUTH_USER_MODEL

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

LOCATION_CHOICES = (
    ('Nairobi', 'Nairobi'),
    ('Kisumu', 'Kisumu'),
    ('Mombasa', 'Mombasa'),
)

DEPARTMENTS = (
    ('FD', 'Fire Department'),
    ('MD', 'Medical Department'),
    ('PD', 'Police Department'),
)
class User(AbstractUser):
    '''Extending the base user'''
    is_admin_status = models.BooleanField(default=False)

class Hood(models.Model, CrudMethods):
    '''Model table for the neighbourhood that a user is assigned'''
    hood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='Nairobi')
    occupants_count = models.IntegerField(default=0)
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hoodadmin', null=True)
    
    def update_hood_admin(self, user):
        '''Overwriting the update class method'''
        if user.is_admin_status == False:
            raise ValueError('User must have admin status to be incharge of a hood')
        self.admin = user
        self.save()

    def __str__(self):
        return self.hood_name

class Profile(models.Model, CrudMethods):
    '''Model table fot the user profile'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, default='User')
    bio = models.TextField(default='Bio')
    profile_picture = CloudinaryField('image', default='https://res.cloudinary.com/mutugiii/image/upload/v1585139495/ben-sweet-2LowviVHZ-E-unsplash_gynjx7.jpg')
    location = models.CharField(max_length=12, choices=LOCATION_CHOICES, default='Nairobi')
    hood = models.OneToOneField(Hood, on_delete=models.CASCADE, related_name='userhood', null=True, blank=True)

    def __str__(self):
        return self.username

class Post(models.Model, CrudMethods):
    '''Model table for posts that are created by the user'''
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_image = CloudinaryField('image', null=True)
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userpost')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hoodposts')

    def __str__(self):
        return self.post_title
class Bussiness(models.Model, CrudMethods):
    '''Model Table for the bussinesses/Facilities'''
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hoodbussinesses')

    def __str__(self):
        return self.name

class EmergencyService(models.Model, CrudMethods):
    '''Model Table for emergency services'''
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    department = models.CharField(max_length=2, choices=DEPARTMENTS, default='FD')
    description = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hoodemergencyservice')

    def __str__(self):
        return '{} of department {}'.format(self.name, self.department)