from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import search
from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField

# Create your models here.

class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credentials = CredentialsField()


class FlowModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    flow = FlowField()


class Search(models.Model):
    search = models.CharField(max_length=128)
    searcher = models.ForeignKey(User)
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ['-pub_date', ]
        verbose_name_plural = 'searches'

    def __unicode__(self):
        return self.search

    def save(self):
        if not self.pk:
         # this object is new, set pub_date
            self.pub_date = timezone.now()
        super(Search, self).save()


class Results(models.Model):
    #result = search.youtube_search(10)

    def __unicode__(self):
        return self.result


class Video(models.Model):
    pass
