from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm
from .models import User, Profession, Team


class UserAdminAuth(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('id', 'username', 'email', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'is_superuser', 'last_login')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email', 'picture', 'brief_introduction'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Interests'), {'fields': ('interests',)}),
        (_('Profession'), {'fields': ('profession',)}),
        (_('Social Accounts'), {'fields': ('facebook_profile', 'instagram_profile',
                                           'linkedin_profile', 'twitter_profile')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    ordering = ('username',)

    filter_horizontal = ['groups', 'user_permissions', 'interests']
    save_on_top = True


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(User, UserAdminAuth)
