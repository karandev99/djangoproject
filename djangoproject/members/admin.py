from django.contrib import admin
from django.apps import apps
from .models import Members

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display= ('id','firstname','lastname')

# Register your models here.
