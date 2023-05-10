from django.db import models

# # Create your models here.

# class UserLink(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     link_category = models.CharField(max_length=100)
#     link = models.URLField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

import qrcode
from io import BytesIO
from django.core.files import File
from django.urls import reverse


class UserLink(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    link_category = models.CharField(max_length=100)
    link = models.URLField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


