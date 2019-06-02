from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import TodoCreateForm
from .models import Todo
from django.urls import reverse_lazy

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoCreateForm
    template_name = 'account/create_todo.html'

class TodoUpdateView(UpdateView): 
    model = Todo
    template_name = 'account/todo_edit.html'
    fields = ['title', 'description', 'status']

class TodoDetailView(DetailView):
    model = Todo
    template_name = "account/todo_details.html"


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'account/todo_delete.html'
    success_url = reverse_lazy('dashboard')
