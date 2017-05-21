from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class First(models.Model):
  title = models.CharField(_('Title'), max_length=15)
  body = models.TextField(_('Body'))
  created = models.DateField(_('Created'), auto_now_add=True)
  modified = models.DateTimeField(_('Modified'), auto_now=True)

  def get_absolute_url(self):
    return reverse('first:view', kwargs={'pk': self.pk})

  def __str__(self):
    format = { 
      'title': self.title, 
      'date': self.created.isoformat()
    }
    return _('{title} created on {date}').format(**format)
