from django.conf.urls import url
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from .views import add_project_view, list_project_view, detail_project_view


urlpatterns = [
    path(_('nuevo/'), add_project_view, name='add_project'),
    path(_('todos/'), list_project_view, name='list_project'),
    path(_('ver/<int:pk>/'), detail_project_view, name='detail_project_view'),
]
