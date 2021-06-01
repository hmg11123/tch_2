from django.contrib import admin
from . import models


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
