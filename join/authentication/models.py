from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import F, CharField, Value
from django.db.models.functions import Coalesce
from django_extensions.db.models import TitleSlugDescriptionModel


class CustomUserManager(UserManager):

    def get_queryset(self, *args, **kwargs):
        qs = super(CustomUserManager, self).get_queryset(*args, **kwargs)

        return qs

    def get_by_natural_key(self, username):
        """
        Return a user from email or username.

        :param username: is username or email
        :return: a user instance
        """
        try:
            user = self.get(**{self.model.USERNAME_FIELD: username})
        except User.DoesNotExist:
            user = self.get(**{self.model.ALTERNATIVE_USERNAME_FIELD: username})
        return user


class User(AbstractUser):

    ALTERNATIVE_USERNAME_FIELD = "email"

    avatar = models.ImageField(blank=True, null=True, upload_to='photos')

    profession = models.ForeignKey('authentication.Profession', blank=True, null=True, on_delete=models.SET_NULL)

    interests = models.ManyToManyField('project.Interest')

    brief_introduction = models.TextField(max_length=150, blank=True, null=True)

    objects = CustomUserManager()


class Profession(TitleSlugDescriptionModel):

    def __str__(self):
        return self.title
