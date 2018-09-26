from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

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

    interests = models.ManyToManyField('project.Interest')

    objects = CustomUserManager()
