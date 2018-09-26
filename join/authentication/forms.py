from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UsernameField
from django.utils.translation import ugettext_lazy as _

from .models import User
from project.models import Interest


class UserChangeForm(forms.ModelForm):

    interests = forms.ModelMultipleChoiceField(
        Interest.objects.all(),
        widget=FilteredSelectMultiple("Interests", True),
        required=False,
    )

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = '__all__'
        exclude = []
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = self.fields['password'].help_text.format('../password/')
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
