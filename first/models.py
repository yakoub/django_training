from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class First(models.Model):
  title = models.CharField(max_length=15)
  body = models.TextField()
  created = models.DateField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  ip = models.GenericIPAddressField(protocol='IPv4')
  mpoly = models.MultiPolygonField(null=True, blank=True)
  objects = models.GeoManager()

  def get_absolute_url(self):
    return reverse('first:view', kwargs={'pk': self.pk})

  def __str__(self):
    return "{0} created on {1}".format(self.title, self.created.isoformat())
