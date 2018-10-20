from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from authentication.models import User
from project.models import Project


class PageView(TemplateView):

    def get_template_names(self):
        template_name = 'pages_templates/{}'.format(self.kwargs.get('page_name', 'index'))
        template_name = template_name if template_name.endswith('.html') else '{}.html'.format(template_name)
        return [template_name]


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['popular_users'] = User.objects.filter(avatar__isnull=False)[:6]
        context['popular_projects'] = Project.objects.all()[:6]
        return context


page_view = PageView.as_view()
home_view = HomeView.as_view()
