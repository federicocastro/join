from django.views.generic import CreateView, ListView, DetailView
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


class DetailProjectView(DetailView):
    template_name = 'project/detail.html'
    model = Project
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        ctx = super(DetailProjectView, self).get_context_data(**kwargs)
        ctx['related_projects'] = Project.objects.all()
        return ctx


add_project_view = AddProjectView.as_view()
list_project_view = ListProjectView.as_view()
detail_project_view = DetailProjectView.as_view()