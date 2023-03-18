from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from exams.models import Course, Unit, Exam


class Student(User):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=+254711111111)

    def __str__(self):
        return f'{self.get_full_name()}'

    class Meta:
        verbose_name = "Student"
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
    phone_number = models.IntegerField(default=+254711111111)

    def __str__(self):
        return f'{self.get_full_name()}'


    class Meta:
        verbose_name_plural = "Parents"



class ExamEnrolled(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
    date_enrolled = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.exams} Exam'
  
    class Meta:
        verbose_name_plural = "ExamsEnrolled"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    # override the save method in order to get the image saved for resizing
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 350 or img.width > 350:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

   