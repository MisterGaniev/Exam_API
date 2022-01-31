from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.


@admin.register(Todo)
class Todo_admin(ModelAdmin):
    pass
