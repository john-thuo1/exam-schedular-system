from django.contrib import admin
from users.models import Profile, Student, Parent, Professor, ExamEnrolled

# Registering users models to the django admin.
admin.site.register(Profile)
admin.site.register(ExamEnrolled)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Professor)

