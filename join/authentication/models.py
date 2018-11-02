from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Count
from photologue.models import Photo

from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from model_utils import Choices

from core.models import ImageField


class CustomUserManager(UserManager):

    def get_queryset(self, *args, **kwargs):
        qs = super(CustomUserManager, self).get_queryset(*args, **kwargs)
        qs = qs.annotate(
            has_projects=Count('my_projects') + Count('projects')
        )

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

    picture = ImageField(blank=True, null=True, upload_to='users-pictures')

    profession = models.ForeignKey('authentication.Profession', blank=True, null=True, on_delete=models.SET_NULL)

    interests = models.ManyToManyField('project.Interest', blank=True)
    skills = models.ManyToManyField('authentication.Skill', related_name='users', blank=True)

    brief_introduction = models.TextField(max_length=150, blank=True, null=True)

    project_views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)

    facebook_profile = models.CharField(max_length=300, blank=True, null=True)
    youtube_profile = models.CharField(max_length=300, blank=True, null=True)
    twitter_profile = models.CharField(max_length=300, blank=True, null=True)
    linkedin_profile = models.CharField(max_length=300, blank=True, null=True)
    gplus_profile = models.CharField(max_length=300, null=True, blank=True)
    instagram_profile = models.CharField(max_length=300, null=True, blank=True)

    def get_facebook_profile_url(self):
        return 'https://www.facebook.com/{}'.format(self.facebook_profile)

    def get_twitter_profile_url(self):
        return 'https://twitter.com/{}'.format(self.twitter_profile)

    def get_linkedin_profile_url(self):
        return 'https://www.linkedin.com/in/{}'.format(self.linkedin_profile)

    def get_gplus_profile_url(self):
        return 'https://www.facebook.com/{}'.format(self.gplus_profile)

    def get_instagram_profile_url(self):
        return 'https://www.instagram.com/{}'.format(self.instagram_profile)

    def get_youtube_profile_url(self):
        return 'https://www.youtube.com/{}'.format(self.youtube_profile)

    objects = CustomUserManager()


class UserFollow(TimeStampedModel):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='following')
    user_followed = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='followed_by')


class Skill(TitleSlugDescriptionModel):

    def __str__(self):
        return self.title


class Profession(TitleSlugDescriptionModel):

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    TEAM_ROLE_CHOICES = Choices(
        ('owner', _('Propietario')),
        ('administrator', _('Administrador')),
        ('collaborator', _('Colaborador')),
    )

    user = models.ForeignKey('authentication.User', on_delete=models.PROTECT)
    team = models.ForeignKey('authentication.Team', on_delete=models.PROTECT)
    role = models.CharField(choices=TEAM_ROLE_CHOICES, default=TEAM_ROLE_CHOICES.collaborator, max_length=30)


class Team(models.Model):
    name = models.CharField(max_length=60)
    members = models.ManyToManyField('authentication.User', through='authentication.TeamMember', related_name='teams')


