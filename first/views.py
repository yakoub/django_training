from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from first.models import First
import logging
logger = logging.getLogger('django')

class FirstCreate(CreateView):
  model = First
  fields = ['title', 'body']

  def get_context_data(self, **kwargs):
    context = super(FirstCreate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('first:create') 
    return context

class FirstUpdate(UpdateView):
  model = First
  fields = ['title', 'body']

  def get_context_data(self, **kwargs):
    context = super(FirstUpdate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('first:view', kwargs={'pk': self.object.pk}) + '/edit'
    return context

class FirstDelete(DeleteView):
  model = First
  success_url = reverse_lazy('list')

  def get_context_data(self, **kwargs):
    context = super(FirstDelete, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('first:view', kwargs={'pk': self.object.pk}) + '/delete'
    return context

class FirstView(DetailView):
  model = First

  def get(self, request, *args, **kwargs):
    logger.info('django view')
    return super(FirstView, self).get(request, args, kwargs)

class FirstList(ListView):
  model = First
  paginate_by = 2
