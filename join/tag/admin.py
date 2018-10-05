from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from .models import TaggedItem


class TaggedItemAdminInline(GenericTabularInline):
    model = TaggedItem


@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'content_object')

    def get_queryset(self, request):
        qs = super(TaggedItemAdmin, self).get_queryset(request)
        qs = qs.select_related('content_object')
        return qs
