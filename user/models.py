from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to="user_avatar/", null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'Profile for | {self.user.get_full_name()}'



