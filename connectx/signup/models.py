from django.db import models

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)
   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProfileLink(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_links')
    link_category = models.CharField(max_length=100,default='')
    link = models.URLField(default='')

    def __str__(self):
        return f"{self.link_category}: {self.link}"
