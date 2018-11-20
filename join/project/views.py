from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from .models import Project
from django import forms


class AddProjectForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Project.STATUS_CHOICES, required=False)

    class Meta:
        model = Project
        fields = ['title', 'brief_description', 'status', 'visibility',
                  'license', 'description', 'collaborators']


class AddProjectView(CreateView):
    template_name = 'project/add.html'
    form_class = AddProjectForm
    model = Project

    def get_success_url(self):
        return reverse('detail_project_view', kwargs={'pk': self.object.id})

    def get_initial(self):
        initial = super(AddProjectView, self).get_initial()
        initial.update(
            {
                'owner': self.request.user,
                'status': Project.STATUS_CHOICES.open
            }
        )
        return initial

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return HttpResponseRedirect(self.get_success_url())


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
        user = self.request.user
        if user.is_authenticated:
            with transaction.atomic():
                user.projects_viewed.add(self.get_object())
        return ctx


add_project_view = AddProjectView.as_view()
list_project_view = ListProjectView.as_view()
detail_project_view = DetailProjectView.as_view()