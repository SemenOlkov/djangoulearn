from django.contrib import admin
from .models import SalaryData

@admin.register(SalaryData)
class SalaryDataAdmin(admin.ModelAdmin):
    list_display = ('year', 'average_salary')
    list_editable = ('average_salary',)
    search_fields = ('year',)