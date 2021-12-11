from django.contrib import admin
from .models import Position, Employee, Service

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'active', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icone', 'active', 'updated_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active', 'updated_at')
    list_filter = ('position',)
    list_editable = ('active',)
    search_fields = ('name',)
    