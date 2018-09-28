from django.views.generic import ListView, DetailView

from authentication.models import User, Profession


class UsersView(ListView):
    template_name = 'users/list-users.html'
    model = User
    pk_url_kwarg = 'pk'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(UsersView, self).get_context_data(*args, object_list=None, **kwargs)
        context['professions'] = Profession.objects.all()
        return context


class UserProfileView(DetailView):
    template_name = 'users/user-profile.html'
    model = User


users_view = UsersView.as_view()
user_profile_view = UserProfileView.as_view()
