from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default="Enter a brief course description")
    


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Unit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default="Enter a description of the Unit")

    def __str__(self):
        return f'{self.name}'
 


class Exam(models.Model):
    start_time = models.TimeField(default=timezone.now)
    duration = models.TextField(default="1hr")
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    def __str__(self):
        # {(self.start_date.strftime("%d-%b-%Y %I:%M:%p"))} to {self.end_date.strftime("%d-%b-%Y %I:%M:%p")}
        return f'{self.unit} Exam at {self.start_time} on {(self.start_date.strftime("%d-%b-%Y"))} for {self.duration} '

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

