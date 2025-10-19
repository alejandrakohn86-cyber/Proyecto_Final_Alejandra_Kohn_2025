from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_creacion', 'fecha_modificacion']
    list_filter = ['fecha_creacion', 'autor']
    search_fields = ['titulo', 'subtitulo', 'contenido']
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
