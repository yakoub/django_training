from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Award(models.Model):
  title = models.CharField(max_length=15)
  amount = models.DecimalField(decimal_places=2, max_digits=6)

  def get_absolute_url(self):
    return reverse('actors:award-view', kwargs= {'pk': self.pk})

  def __unicode__(self):
    return self.title

class Actress(models.Model):
  name = models.CharField(max_length=15)
  bio = models.TextField()
  awards = models.ManyToManyField(Award)

  def get_absolute_url(self):
    return reverse('actors:view', kwargs= {'pk': self.pk})

  def __unicode__(self):
    return self.name

