from django.views.generic.base import TemplateView
from django.views.generic import ListView
from authentication.models import User


class UsersView(ListView):
    template_name = 'users/list-users.html'
    model = User


class UserProfileView(TemplateView):
    template_name = 'users/user-profile.html'


users_view = UsersView.as_view()
user_profile_view = UserProfileView.as_view()
