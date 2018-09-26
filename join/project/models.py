from django.db import models
from core.models import TimeStampedModel, TitleDescriptionModel, TitleSlugDescriptionModel


class Project(TimeStampedModel, TitleDescriptionModel):
    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='my_projects')
    collaborators = models.ManyToManyField('authentication.User', related_name='projects')
    gallery = models.OneToOneField('photologue.Gallery', on_delete=models.CASCADE, related_name='extended',
                                   blank=True, null=True)


class Interest(TitleSlugDescriptionModel):

    def __str__(self):
        return self.title
