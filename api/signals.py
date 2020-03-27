# File to save signals for profile & delete objects from cloudinary
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
import cloudinary
from .models import Profile

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     '''Signal to check if a User is saved & creates a Profile'''
#     if created:
#         Profile.objects.create(name=instance.username, user=instance)