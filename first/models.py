from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class First(models.Model):
  title = models.CharField(max_length=15)
  body = models.TextField()

  def get_absolute_url(self):
    return reverse('first-view', kwargs={'pk': self.pk})
