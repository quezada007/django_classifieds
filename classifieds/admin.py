from django.contrib import admin

from .models import Classified


@admin.register(Classified)
class ClassifiedAdmin(admin.ModelAdmin):
    list_display = ['category', 'first_name', 'last_name', 'location', 'title', 'price', 'submission_date']
