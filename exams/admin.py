from django.contrib import admin
from django.contrib import admin
from exams.models import Unit, Course, Exam

# Registering models for our project

admin.site.register(Unit)
admin.site.register(Course)
admin.site.register(Exam)
