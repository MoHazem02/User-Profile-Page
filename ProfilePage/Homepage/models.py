from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    facebook_account = models.CharField(max_length=255, null=True, blank=True)
    twitter_account = models.CharField(max_length=255, null=True, blank=True)
    linkedin_account = models.CharField(max_length=255, null=True, blank=True)
    github_account = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    faculty = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)


class Posts(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.text
