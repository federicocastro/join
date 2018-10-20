from django.conf.urls import url
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from .views import add_project_view, list_project_view, detail_project_view


urlpatterns = [
    url(_(r'^add/'), add_project_view, name='add_project'),
    url(_(r'^list/'), list_project_view, name='list_project'),
    path(_(r'^view/<int:pk>/'), detail_project_view, name='detail_project_view'),
]
