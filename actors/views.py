from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from actors.models import Actress, Award 

#----
class ActressFormMixin:

  def get_template_names(self):
    return ['actors/form.html', 'form.html']

#----
class ActressCreate(ActressFormMixin, CreateView):
  model = Actress
  fields = ['name', 'bio', 'awards']

  def get_context_data(self, **kwargs):
    context = super(ActressCreate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('actors:create') 
    return context

#----
class ActressUpdate(ActressFormMixin, UpdateView):
  model = Actress
  fields = ['name', 'bio', 'awards']

  def get_context_data(self, **kwargs):
    context = super(ActressUpdate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('actors:view', kwargs={'pk': self.object.pk}) + 'edit'
    return context

#----
class ActressDelete(DeleteView):
  model = Actress
  success_url = reverse_lazy('list')

  def get_context_data(self, **kwargs):
    context = super(ActressDelete, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('actors:view', kwargs={'pk': self.object.pk}) + '/delete'
    return context

#----
class ActressView(DetailView):
  model = Actress

  def get_context_data(self, **kwargs):
    context = super(ActressView, self).get_context_data(**kwargs)
    context['awards'] = self.object.awards.all()
    return context
#----
class ActressList(ListView):
  model = Actress
  paginate_by = 4

  def get_template_names(self):
    return ['actors/list.html', 'list.html']

  def get_queryset(self):
    queryset = super(ActressList, self).get_queryset()
    queryset.prefetch_related('awards')
    return queryset

#---- Award
class AwardCreate(CreateView):
  model = Award
  fields = ['title', 'amount']
  template_name = 'form.html'

  def get_context_data(self, **kwargs):
    context = super(AwardCreate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('actors:award-create') 
    return context

#----
class AwardUpdate(UpdateView):
  model = Award
  fields = ['title', 'amount']
  template_name = 'form.html'

  def get_context_data(self, **kwargs):
    context = super(AwardUpdate, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('actors:award-view', kwargs={'pk': self.object.pk}) + 'edit'
    return context

#----
class AwardDelete(DeleteView):
  model = Award
  success_url = reverse_lazy('list')

  def get_context_data(self, **kwargs):
    context = super(AwardDelete, self).get_context_data(**kwargs)
    context['action'] = reverse_lazy('actors:award-view', kwargs={'pk': self.object.pk}) + '/delete'
    return context

#----
class AwardView(DetailView):
  model = Award

  def get_context_data(self, **kwargs):
    context = super(AwardView, self).get_context_data(**kwargs)
    context['actresses'] = self.object.actress_set.all()
    return context;
#----
class AwardsList(ListView):
  model = Award
  paginate_by = 2

  def get_template_names(self):
    return ['actors/award_list.html', 'list.html']

  def get_queryset(self):
    queryset = super(AwardsList, self).get_queryset()
    queryset.prefetch_related('actress_set')
    return queryset
