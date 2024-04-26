from django.contrib import admin
from .models import Student, Professor, Course, Grade


admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Grade)