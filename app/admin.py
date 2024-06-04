from django.contrib import admin

# Register your models here.
from .models import Clients

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'telegram_id', 'created']
    search_fields = ['name', 'surname', 'telegram_id']
