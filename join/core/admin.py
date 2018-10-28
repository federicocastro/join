from django.contrib import admin
from .models import File, ImageTitleSlug, Image


@admin.register(ImageTitleSlug)
class ImageTitleSlugAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file', 'type', 'uploaded_by')
    search_fields = ('name', 'id', 'type', 'uploaded_by')

    def get_queryset(self, request):
        qs = super(FileAdmin, self).get_queryset(request)
        qs = qs.select_realated('uploaded_by')
        return qs
