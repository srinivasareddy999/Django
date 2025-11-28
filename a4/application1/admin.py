from django.contrib import admin
from application1.models import student
class student_admin(admin.ModelAdmin):
    list_display=['sid','sname','sec','J_date','gender']
admin.site.register(student,student_admin)
