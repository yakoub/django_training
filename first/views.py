from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.utils import translation
from first.models import First
import logging
logger = logging.getLogger('django')
import json

#----
class FirstFormMixin:

  def get_template_names(self):
    return ['first/form.html', 'form.html']

#----
class FirstCreate(FirstFormMixin, CreateView):
  model = First
  fields = ['title', 'body', 'ip', 'mpoly'] #

  def get_context_data(self, **kwargs):
    context = super(FirstCreate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('first:create') 
    context['jsconfig'] = json.dumps({'count':4, 'id': 'item3'})
    return context

#----
class FirstUpdate(FirstFormMixin, UpdateView):
  model = First
  fields = ['title', 'body', 'mpoly']

  def get_context_data(self, **kwargs):
    context = super(FirstUpdate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('first:view', kwargs={'pk': self.object.pk}) + 'edit'
    return context

#----
class FirstDelete(DeleteView):
  model = First
  success_url = reverse_lazy('list')

  def get_context_data(self, **kwargs):
    context = super(FirstDelete, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('first:view', kwargs={'pk': self.object.pk}) + '/delete'
    return context

#----
class FirstView(DetailView):
  model = First

  def get_object(self, queryset=None):
    logger.error('kwargs type = {0}'.format(type(self.kwargs)))
    return super(FirstView, self).get_object(queryset)
    
  def get_context_data(self, **kwargs):
    context = super(FirstView, self).get_context_data(**kwargs)
    context['type'] = repr(self.object.mpoly.__class__)
    current_language = translation.get_language()
    language_switch = [(code, name) for code, name in settings.LANGUAGES if code != current_language]
    context['language_switch'] = language_switch 
    return context
    
  def get(self, request, *args, **kwargs):
    logger.info('django view')
    return super(FirstView, self).get(request, args, kwargs)

#----
class FirstList(ListView):
  model = First
  paginate_by = 2

  def get_template_names(self):
    return ['first/list.html', 'list.html']
