from django.contrib import admin
from .models import Slide


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_public', 'show_btn', 'btn_link', 'image')
    list_editable = ('show_btn',)
