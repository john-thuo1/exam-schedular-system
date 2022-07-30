from django.contrib import admin
from users.models import OTP, Profile, Student, Parent, Professor, ExamEnrolled

# Register your models here.
admin.site.register(Profile)
admin.site.register(ExamEnrolled)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Professor)
admin.site.register(OTP)
