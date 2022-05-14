from distutils.command import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    idade = models.IntegerField(default=None, blank=True, null=True)
    peso = models.IntegerField(default=None, blank=True, null=True)
    altura = models.IntegerField(default=None, blank=True, null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default=None, blank=True, null=True)
    especialidade = models.TextField(default=None, blank=True, null=True)
    objetivo = models.TextField(default=None, blank=True, null=True)
    def __str__(self):
        return self.user.username

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


class displayclients(models.Model):
    username=models.CharField(max_length=100)