
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from api.generate_code import get_code
from users.forms import UserRegisterForm, UserUpdateForm, OTPForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from users.models import OTP, Student, Professor, Parent, ExamEnrolled
from django.contrib import messages
from django.contrib.auth import login, logout
# from api.signals import booking_code
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)

# from django.contrib.auth.mixins import LoginRequiredMixin
from exams.models import Exam
from django.shortcuts import get_object_or_404
import api.send_message as send_message


# the view to be displayed after a user successfully registers
def account_created(request):
    return render(request, 'users/account_created.html')    


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context=context)


# -------------------------------------------------------------------------------------------------------------------------
# Student Views

class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'username', 'course', 'phone_number']
    template_name = 'users/student_detail.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Student'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'username', 'course', 'phone_number']
    template_name = 'users/student_detail.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Student'
        return context


class StudentListView(ListView):
    model = Student
    template_name = 'users/students_list.html'
    context_object_name = 'students'


class StudentDeleteView(DeleteView):
    model = Student
    context_object_name = 'student'
    template_name = 'exams/confirm_delete.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Student'
        student_name = Student.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the following student: "{student_name}"?'
        context['cancel_url'] = 'students-list'
        return context


# -----------------------------------------------------------------------------------------------------------------------
# Professor Views

class ProfessorCreateView(CreateView):
    model = Professor
    fields = ['first_name', 'last_name', 'email','phone_number','username', 'unit']
    template_name = 'users/professor_detail.html'

    def get_success_url(self):
        return reverse('professors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Professor'
        return context


class ProfessorUpdateView(UpdateView):
    model = Professor
    fields = ['first_name', 'last_name', 'email', 'phone_number','username', 'unit']
    template_name = 'users/professor_detail.html'

    def get_success_url(self):
        return reverse('professors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Professor'
        return context


class ProfessorListView(ListView):
    model = Professor
    template_name = 'users/professors_list.html'
    context_object_name = 'professors'


class ProfessorDeleteView(DeleteView):
    model = Professor
    context_object_name = 'professor'
    template_name = 'exams/confirm_delete.html'

    def get_success_url(self):
        return reverse('professors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Professor'
        professor_name = Professor.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the following Professor "{professor_name}" ?'
        context['cancel_url'] = 'professors-list'
        return context


# ----------------------------------------------------------------------------------------------------------------------
# Parent Views

class ParentCreateView(CreateView):
    model = Parent
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'students']
    template_name = 'users/parent_detail.html'

    def get_success_url(self):
        return reverse('parents-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Parent'
        return context


class ParentUpdateView(UpdateView):
    model = Parent
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'students']
    template_name = 'users/parent_detail.html'

    def get_success_url(self):
        return reverse('parents-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Parent'
        return context


class ParentListView(ListView):
    model = Parent
    template_name = 'users/parents_list.html'
    context_object_name = 'parents'


class ParentDeleteView(DeleteView):
    model = Parent
    context_object_name = 'parent'
    template_name = 'exams/confirm_delete.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('parents-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Parent'
        parent_name = Parent.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the following parent "{parent_name}"?'
        context['cancel_url'] = 'parents-list'
        return context


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ExamEnroll Views

class ExamEnrollListView(ListView):
    model = ExamEnrolled
    template_name = 'users/exam_enroll_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registered_students = ExamEnrolled.objects.filter(exams_id=self.kwargs.get('exam_id'))
        exam_name = get_object_or_404(Exam, pk=self.kwargs.get('exam_id'))
        
        context['enrolled_students'] = registered_students
        context['exam_name'] = f'{exam_name.unit.name} Exam Student List'
        # context['Exam Booking Code'] = booking_code
        return context


class ExamEnrollCreateView(CreateView):
    model = ExamEnrolled
    fields = ['exams', 'student']
    template_name = 'users/exam_enroll_detail.html'

    def get_success_url(self):
        return reverse('exams-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = f'Student Exam Registration'
        context['btn_label'] = 'Register'
        return context


class ExamEnrolledUpdateView(UpdateView):
    model = ExamEnrolled
    fields = ['marks']
    template_name = 'users/exam_enroll_detail.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('enrolled-students-list', kwargs={'exam_id': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Student Grade'
        context['btn_label'] = 'Update'
        return context

    def post(self, request, *args, **kwargs):
        exam_enrolled_id = self.kwargs.get('pk')
        exam_enrolled = ExamEnrolled.objects.get(pk=exam_enrolled_id)

        super().post(request, *args, **kwargs)

        if exam_enrolled.marks != request.POST.get('marks'):
            student = self.get_object().student
            exam = self.get_object().exams
            parent = student.parent_set.first()
            message_to_parent = f'Dear Parent,\n'\
              f'Your Child, {student.get_full_name()} scored {request.POST.get("marks")}% in {exam.unit.name} Exam for {exam.unit.course} Course.'
            message_to_student = f'Dear {student.get_full_name()},\n'\
              f'You scored  {request.POST.get("marks")}% in {exam.unit.name} Exam for {exam.unit.course} Course.'
            send_message.send(student.phone_number, message_to_student)
            send_message.send(parent.phone_number, message_to_parent)

        return redirect('enrolled-students-list', exam_id=exam_enrolled.exams_id)


class ExamEnrolledDeleteView(DeleteView):
    model = ExamEnrolled
    template_name = 'exams/confirm_delete.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('exams-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Student Enrollment and Grades'
        exam_enrolled = ExamEnrolled.objects.get(pk=self.kwargs.get('pk'))
        context[
            'message'] = f'Are you sure you want to remove "{exam_enrolled.student.get_full_name()}" from the exam list ?'
        context['cancel_url'] = 'exams-list'
        return context


