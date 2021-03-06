from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel, TitleDescriptionModel, TitleSlugDescriptionModel
from model_utils import Choices

from tag.models import TaggedItem

from core.models import Image, Comment


class ProjectImage(Image):
    project = models.ForeignKey('project.Project', related_name='images', on_delete=models.CASCADE)


class ProjectComment(Comment):
    project = models.ForeignKey('project.Project', related_name='comments', on_delete=models.CASCADE)


class Project(TimeStampedModel, TitleDescriptionModel):
    STATUS_CHOICES = Choices(
        ('open', _('Open')),
        ('initiated', _('Initiated')),
        ('finished', _('Finished')),
    )
    VISIBILITY_CHOICES = Choices(
        ('public', _('Public')),
        ('private', _('Private')),
    )

    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='my_projects')
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES.open, max_length=40)
    visibility = models.CharField(choices=VISIBILITY_CHOICES, default=VISIBILITY_CHOICES.public, max_length=30)

    brief_description = models.CharField(null=True, blank=True, max_length=130)
    collaborators = models.ManyToManyField('authentication.User', related_name='projects')

    followed_by = models.ManyToManyField('authentication.User', related_name='projects_followed')
    liked_by = models.ManyToManyField('authentication.User', related_name='projects_liked')
    viewed_by = models.ManyToManyField('authentication.User', related_name='projects_viewed')

    license = models.ForeignKey('project.License', null=True, blank=True, on_delete=models.PROTECT)

    tags = GenericRelation(TaggedItem)

    def get_primary_image_url(self):
        first_image = self.get_primary_image()
        url = first_image.url if first_image else 'http://via.placeholder.com/550x700'
        return url

    def get_primary_image(self):
        first_image = self.images.first()
        return first_image.file if first_image else None


class Interest(TitleSlugDescriptionModel):

    def __str__(self):
        return self.title


class License(TitleSlugDescriptionModel):
    file = models.FileField(upload_to='licenses')

    tags = GenericRelation(TaggedItem)
