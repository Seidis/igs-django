from django.contrib import admin

from hr.models import Employee, Department


class Employees(admin.ModelAdmin):
    list_display = ("id", "name", "department")
    list_display_links = ("id", "name")
    search_fields = ("name", "department")
    list_per_page = 10


class Departments(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 10


admin.site.register(Employee, Employees)
admin.site.register(Department, Departments)
