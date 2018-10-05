from django.contrib import admin
from tag.admin import TaggedItemAdminInline
from .models import Project, Interest


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'owner')
    search_fields = ('id', 'title', 'description', 'owner')
    inlines = (TaggedItemAdminInline,)

    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)
        qs = qs.select_related('owner')
        return qs


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')


class InterestInlineAdmin(admin.TabularInline):
    model = Interest
