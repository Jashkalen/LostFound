from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Item
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ItemListView(ListView):
    model = Item
    context_object_name = 'item'
    template_name = 'app/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'app/item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['type', 'title', 'description', 'location', 'date', 'contact_email', 'user' ]
    template_name = 'app/item_create.html'

    def grt_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context



class ItemUpdateView(UpdateView):
    model = Item
    fields = ['type', 'title', 'description', 'image', 'location', 'date', 'contact_email', 'user']
    template_name = 'app/item_update.html'

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'app/item_delete.html'
    success_url = reverse_lazy('item')

    def homepage(request):
        return render(request, 'app/home.html')

