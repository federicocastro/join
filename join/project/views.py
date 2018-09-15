from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView
from .models import Project


class AddProjectView(CreateView):
    template_name = 'project/add.html'
    model = Project
    fields = ['title', 'description', 'collaborators', 'gallery']
    
    def form_valid(self, form):
        super(AddProjectView, self).form_valid(form)


class ListProjectView(ListView):
    template_name = 'project/list.html'
    model = Project


add_project_view = AddProjectView.as_view()
list_project_view = ListProjectView.as_view()
