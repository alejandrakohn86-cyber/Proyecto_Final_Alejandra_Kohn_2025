from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['asunto', 'remitente', 'destinatario', 'fecha_envio', 'leido']
    list_filter = ['leido', 'fecha_envio']
    search_fields = ['asunto', 'contenido', 'remitente__username', 'destinatario__username']
    readonly_fields = ['fecha_envio']
