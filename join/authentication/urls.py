from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from .views import users_view, user_profile_view


urlpatterns = [
    url(_(r'^profile/<int:id>'), user_profile_view, name='user_profile'),
    url(_(r'^find/'), users_view, name='find_users'),
]
