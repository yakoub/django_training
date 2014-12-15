from django.views.generic.edit import DeleteView, FormView
from django.views.generic import DetailView, ListView
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from article.models import Article, Paragraph 
from django import forms
import logging
logger = logging.getLogger('django')

class ParagraphForm(ModelForm):
  class Meta:
    model = Paragraph
    fields = ('content',)
 
  def save(self, commit=True):
    if (self.cleaned_data['ORDER'] is None):
      self.instance.ordinal = 0
    else :
      self.instance.ordinal = self.cleaned_data['ORDER']
    instance = super(ParagraphForm, self).save(commit)
    return instance

def ArticleCreate(request):
  articleForm = modelform_factory(Article, fields=('title', 'view_mode'))
  formset_config = {
    'can_delete': True, 
    'can_order': True,
    'extra': 3,
    'form': ParagraphForm,
  }
  paragraphFormset = modelformset_factory(Paragraph, **formset_config)

  context = RequestContext(request)
  context['action'] = reverse_lazy('articles:create')
  queryset = Paragraph.objects.none()
  if (request.method == 'POST'):
    article_form = articleForm(request.POST, prefix='article')
    paragraphs = paragraphFormset(request.POST, prefix='paragraphs', queryset=queryset)
    if (article_form.is_valid() and paragraphs.is_valid()) :
      article = article_form.save()
      paragraph_instances = paragraphs.save(False)
      for instance in paragraph_instances :
        instance.article = article
      Paragraph.objects.bulk_create(paragraph_instances)
      return HttpResponseRedirect(article.get_absolute_url())
    else :
      context['article'] = article_form 
      context['paragraphs'] = paragraphs
  else:
    context['article'] = articleForm(prefix='article')
    context['paragraphs'] = paragraphFormset(prefix='paragraphs', queryset=queryset)
  return render_to_response(['article/form.html', 'form.html'], context)

def ArticleUpdate(request, pk):
  articleForm = modelform_factory(Article, fields=('title', 'view_mode'))
  formset_config = {
    'can_delete':True, 
    'can_order':True,
    'form': ParagraphForm,
  }
  paragraphFormset = inlineformset_factory(Article, Paragraph, **formset_config)

  context = RequestContext(request)
  context['action'] = reverse_lazy('articles:update', kwargs={'pk': pk})
  article = Article.objects.get(id=pk)
  queryset = Paragraph.objects.order_by('ordinal')
  if (request.method == 'POST'):
    article_form = articleForm(request.POST, instance=article, prefix='article')
    paragraphs = paragraphFormset(request.POST, instance=article, prefix='paragraphs', queryset=queryset)
    if (article_form.is_valid() and paragraphs.is_valid()) :
      article_form.save()
      paragraphs.save()
      return HttpResponseRedirect(article.get_absolute_url())
    else :
      context['article'] = article_form 
      context['paragraphs'] = paragraphs
  else:
    context['article'] = articleForm(instance=article, prefix='article')
    context['paragraphs'] = paragraphFormset(instance=article, prefix='paragraphs', queryset=queryset)

  return render_to_response(['article/form.html', 'form.html'], context)

#----
class ArticleDelete(DeleteView):
  model = Article
  success_url = reverse_lazy('list')

  def get_context_data(self, **kwargs):
    context = super(ArticleDelete, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('articles:view', kwargs={'pk': self.object.pk}) + '/delete'
    return context

#----
class ArticleView(DetailView):
  model = Article

  def get_context_data(self, **kwargs):
    context = super(ArticleView, self).get_context_data(**kwargs)
    context['paragraphs'] = self.object.paragraph_set.all()
    return context;
#----
class ArticleList(ListView):
  model = Article
  paginate_by = 4

  def get_template_names(self):
    return ['article/list.html', 'list.html']
