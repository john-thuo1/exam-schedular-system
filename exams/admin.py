from django.contrib import admin
from django.contrib import admin
from exams.models import Unit, Course, Exam

# Registering models to the Admin 

admin.site.register(Unit)
admin.site.register(Course)
admin.site.register(Exam)
