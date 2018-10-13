from django.views.generic import CreateView, ListView
from .models import Project


class AddProjectView(CreateView):
    template_name = 'project/add.html'
    model = Project
    fields = [
        'title', 'brief_description', 'status', 'visibility',
        'license', 'description', 'collaborators', 'gallery'
    ]

    def form_valid(self, form):
        return super(AddProjectView, self).form_valid(form)


class ListProjectView(ListView):
    template_name = 'project/list.html'
    model = Project


add_project_view = AddProjectView.as_view()
list_project_view = ListProjectView.as_view()
