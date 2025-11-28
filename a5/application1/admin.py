from django.contrib import admin
from application1.models import employees
class employees_admin(admin.ModelAdmin):
    list_display=['eid','ename','company','des','location','salary']
admin.site.register(employees,employees_admin)
