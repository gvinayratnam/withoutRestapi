from django.contrib import admin
from .models import Employee
# Register your models here.

# admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal']

admin.site.register(Employee,EmployeeAdmin)