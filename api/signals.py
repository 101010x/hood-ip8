# File to save signals for profile & delete objects from cloudinary
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
import cloudinary
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''Signal to check if a User is saved & creates a Profile'''
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''Signal to save the profile if User object is saved'''
    instance.profile.save()

@receiver(pre_delete, sender=Profile)
def profile_delete(sender, instance, **kwargs):
    '''To delete the profile & specifically profile image from cloudinary'''
    cloudinary.uploader.destroy(instance.profile_picture.public_id)