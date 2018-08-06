from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class PageView(TemplateView):

    def get_template_names(self):
        template_name = 'pages_templates/{}'.format(self.kwargs.get('page_name', 'index'))
        template_name = template_name if template_name.endswith('.html') else '{}.html'.format(template_name)
        return [template_name]


class HomeView(TemplateView):
    template_name = 'home/home.html'


page_view = PageView.as_view()
home_view = HomeView.as_view()
