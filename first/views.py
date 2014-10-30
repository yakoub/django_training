from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from first.models import First

class FirstCreate(CreateView):
  model = First
  fields = ['title', 'body']

class FirstUpdate(UpdateView):
  model = First
  fields = ['title', 'body']

class FirstDelete(DeleteView):
  model = First
  success_url = reverse_lazy('first-list')

class FirstView(DetailView):
  model = First

class FirstList(ListView):
  model = First
