from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class First(models.Model):
  title = models.CharField(max_length=15)
  body = models.TextField()
  created = models.DateField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def get_absolute_url(self):
    return reverse('first:view', kwargs={'pk': self.pk})

  def __unicode__(self):
    return "{0} created on {1}".format(self.title, self.created.isoformat())
