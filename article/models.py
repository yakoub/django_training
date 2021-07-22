from django.db import models
from django.urls import reverse

class Paragraph(models.Model):
  content = models.TextField()
  ordinal = models.IntegerField()
  article = models.ForeignKey('Article', models.CASCADE)

  def get_absolute_url(self):
    return reverse('articles:list') + '#content/{0}/{1}'.format(self.article.pk, self.pk)

class Article(models.Model):
  title = models.CharField(max_length=15)
  view_mode_list = (
    ('slider', 'Slider'),
    ('scroller', 'Scroller'),
  )
  view_mode = models.CharField(max_length=15, choices=view_mode_list)

  def get_absolute_url(self):
    return reverse('articles:list') + '#content/{0}'.format(self.pk) 

  def __str__(self):
    return self.title

