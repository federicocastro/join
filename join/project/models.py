from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel, TitleDescriptionModel, TitleSlugDescriptionModel
from model_utils import Choices

from tag.models import TaggedItem


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

    gallery = models.OneToOneField('photologue.Gallery', on_delete=models.CASCADE, related_name='extended',
                                   blank=True, null=True)

    license = models.ForeignKey('project.License', null=True, blank=True, on_delete=models.PROTECT)

    tags = GenericRelation(TaggedItem)

    def get_primary_image_url(self):
        url = 'http://via.placeholder.com/550x700'
        gallery = self.gallery
        if gallery and gallery.photos.count():
            photo = gallery.photos.first()
            url = photo.image.url
        return url


class Interest(TitleSlugDescriptionModel):

    def __str__(self):
        return self.title


class License(TitleSlugDescriptionModel):
    file = models.FileField(upload_to='licenses')

    tags = GenericRelation(TaggedItem)
