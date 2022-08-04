from django.db.models.signals import post_save
import api.send_message as send_message
from django.dispatch import receiver
from api.generate_code import get_code

from users.models import ExamEnrolled


@receiver(post_save, sender=ExamEnrolled)
def student_exam_registration(sender, instance, created, **kwargs):
    if created:
        # Get the student name
        student = instance.student
        # Get the Registered Exam 
        exam = str(instance.exams)

        global booking_code
        booking_code = get_code()
        # parent = student.objects.prefetch_related('students').all()
        parent = student.parent_set.first()
        message_to_student =   f'Dear {student.get_full_name()},'\
                    f'You have registered for  {exam}.'\
                    f'The Exam Booking Code is : {booking_code}.'\
                    f'Please make sure you provide this Exam Booking Code on the day of the Exam.\n'\
                    f'If you dont, you wont be allowed in the Examination Room'

        message_to_parent = f'Dear Parent,'\
                  f'Your Child, {student.get_full_name()} has registered for {exam}.\n'\
                  f'The Exam Booking Code is : {booking_code}.'\
                  f'Please remind your child to provide this booking code on the day of Exam.\n'\
                  f'Failure to which they will not be allowed to the Examination Room.\n'
        send_message.send(student.phone_number, message_to_student)
        send_message.send(parent.phone_number, message_to_parent)


# @receiver(post_save, sender=ExamEnrolled)
# def student_exam_registration(sender, instance, created, **kwargs):
#     if created:
#         # Get the student name
#         student = instance.student
#         # Get the Registered Exam 
#         exam = str(instance.exams)
#         # parent = student.objects.prefetch_related('students').all()

#         parent = student.parent_set.first()
#         message = f'Dear Parent,'\
#                   f'Your Child, {student.get_full_name()} has registered for {exam}.\n'\
#                   f'The Exam Booking Code is : {booking_code}.'\
#                   f'Please remind your child to provide this booking code on the day of Exam.\n'\
#                   f'Failure to which they will not be allowed to the Examination Room.\n'
#         send_message.send(parent.phone_number, message)