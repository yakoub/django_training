from django.db import models
from django.core.urlresolvers import reverse

class Paragraph(models.Model):
  content = models.TextField()
  ordinal = models.IntegerField()
  article = models.ForeignKey('Article')

  def get_absolute_url(self):
    suffix = '{0}/{1}/{2}'.format(self.article.view_mode, self.article.pk, self.pk)
    return reverse('articles:list') + '#content/' + suffix

class Article(models.Model):
  title = models.CharField(max_length=15)
  view_mode_list = (
    ('slider', 'Slider'),
    ('scroller', 'Scroller'),
  )
  view_mode = models.CharField(max_length=15, choices=view_mode_list)

  def get_absolute_url(self):
    suffix = '{0}/{1}'.format(self.view_mode, self.pk)
    return reverse('articles:list') + '#content/' + suffix

  def __unicode__(self):
    return self.title

