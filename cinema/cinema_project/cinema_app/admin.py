from django.contrib import admin
from .models import Cinema
from .forms import CinemaForm, CinemaAdminForm

class CinemaAdmin(admin.ModelAdmin):
    form = CinemaAdminForm

admin.site.register(Cinema, CinemaAdmin)
