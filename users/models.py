from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from exams.models import Course, Unit, Exam




class systemUser(User):

    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)




# Create your models here



class Student(systemUser):
    # uniqueId = models.CharField(null=True, blank=True, max_length=100)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=+254711111111)



    def __str__(self):
        return f'{self.get_full_name()}'
    
    # def save(self, *args, **kwargs):
    #     if self.uniqueId is None:
    #         self.uniqueId = str(uuid4()).split('-')[4]
    #     super(Student, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Students"


class Professor(User):

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=+254711111111)



    def __str__(self):
        return f'{self.get_full_name()}'

 
        
    class Meta:
        verbose_name_plural = "Professors"

class Parent(User):

    students = models.ForeignKey('Student', on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.get_full_name()}'


    class Meta:
        verbose_name_plural = "Parents"



class ExamEnrolled(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
    date_enrolled = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.exams} Exam'
  
    class Meta:
        verbose_name_plural = "ExamsEnrolled"

class OTP(models.Model):
    otp_code = models.CharField(null=True, max_length=6)
    user = models.ForeignKey(Exam, related_name= 'OTPClient', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.otp_code}'

    class Meta:
        verbose_name_plural = 'OTP'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)



