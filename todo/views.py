from django.shortcuts import render,redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import TodoModelForm
from .models import TodoModel


class TodoListView(ListView):
    model = TodoModel
    template_name = 'main/home.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        data = TodoModel.objects.filter(title__icontains=q, description__icontains=q)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['title'] = "Home Page"
        return context

class TodoCreateView(CreateView):
    template_name = 'main/create.html'
    form_class = TodoModelForm
    success_url = '/'


class TodoUpdateView(UpdateView):
    model = TodoModel
    template_name = 'main/update.html'
    form_class = TodoModelForm
    success_url = '/'

class TodoDetailView(DetailView):
    model = TodoModel
    template_name = 'main/detail.html'
    context_object_name = 'post'



def delete(request, id):
    TodoModel.objects.get(id=id).delete()
    return redirect("s_orca:list")


