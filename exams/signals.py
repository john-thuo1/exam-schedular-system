from django.db.models.signals import post_save
import exams.send_message as send_message
from django.dispatch import receiver
from users.models import ExamEnrolled


@receiver(post_save, sender=ExamEnrolled)
def student_exam_enrollment(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        exam = str(instance.exams)
        # parent = student.objects.prefetch_related('students').all()

        parent = student.parent_set.first()
        message = f'{student.get_full_name()} has registered for {exam}'
        send_message.send(parent.phone_number, message)