import imp
from django.contrib import admin
from .models import Resume
# Register your models here.
@admin.register(Resume)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address']