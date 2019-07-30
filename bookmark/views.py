from django.views.generic.list import ListView


from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

