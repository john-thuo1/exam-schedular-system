from django.db import models
from django.utils import timezone

# exams models.

# Each course can have multiple units associated with
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the course.")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Unit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the Unit.")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


# If related unit instance is deleted, then delete all associated Exam instances
class Exam(models.Model):
    start_time = models.TimeField(default=timezone.now)
    duration = models.TextField(default="1hr")
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        # Start date formatting as day-month-year
        return f'{self.unit} Exam at {self.start_time} on {(self.start_date.strftime("%d-%b-%Y"))} for {self.duration}'

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
