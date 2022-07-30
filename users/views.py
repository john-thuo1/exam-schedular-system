from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User

from users.forms import UserRegisterForm, UserUpdateForm, OTPForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from users.models import OTP, Student, Professor, Parent, ExamEnrolled
from django.contrib import messages
from users.send_message import send
from users.generate_code import get_code
from django.contrib.auth import login, logout

from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)

# from django.contrib.auth.mixins import LoginRequiredMixin
from exams.models import Exam
from django.shortcuts import get_object_or_404
import exams.send_message as send_message


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
    fields = ['first_name', 'last_name', 'email', 'username', 'course']
    template_name = 'users/student_detail.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Student'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'username', 'course']
    template_name = 'users/student_detail.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
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
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Student'
        student_name = Student.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the student "{student_name}"'
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
        # Call the base implementation first to get a context
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
        # Call the base implementation first to get a context
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
        context['message'] = f'Are you sure you want to delete Professor "{professor_name}" ?'
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
        # Call the base implementation first to get a context
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
        # Call the base implementation first to get a context
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
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Parent'
        parent_name = Parent.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the parent "{parent_name}"'
        context['cancel_url'] = 'parents-list'
        return context


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ExamEnroll Views

class ExamEnrollListView(ListView):
    model = ExamEnrolled
    template_name = 'users/exam_enroll_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enrolled_students = ExamEnrolled.objects.filter(exams_id=self.kwargs.get('exam_id'))
        exam_name = get_object_or_404(Exam, pk=self.kwargs.get('exam_id'))
        context[
            'exam_duration'] = f'From: {exam_name.start_date.strftime("%d-%b-%Y %I:%M:%p")} - To: {exam_name.end_date.strftime("%d-%b-%Y %I:%M:%p")}'
        context['enrolled_students'] = enrolled_students
        context['exam_name'] = f'{exam_name.unit.name} Exam List'
        return context


class ExamEnrollCreateView(CreateView):
    model = ExamEnrolled
    fields = ['exams', 'student']
    template_name = 'users/exam_enroll_detail.html'

    def get_success_url(self):
        return reverse('exams-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = f'Student Exam Enrollment'
        context['btn_label'] = 'Enroll'
        return context


class ExamEnrolledUpdateView(UpdateView):
    model = ExamEnrolled
    fields = ['marks']
    template_name = 'users/exam_enroll_detail.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('enrolled-students-list', kwargs={'exam_id': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
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
            message = f'{student.get_full_name()} got {request.POST.get("marks")}% in {exam.unit.name} Exam'
            send_message.send(parent.phone_number, message)

        return redirect('enrolled-students-list', exam_id=exam_enrolled.exams_id)


class ExamEnrolledDeleteView(DeleteView):
    model = ExamEnrolled
    template_name = 'exams/confirm_delete.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('exams-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Student Enrollment and Grades'
        exam_enrolled = ExamEnrolled.objects.get(pk=self.kwargs.get('pk'))
        context[
            'message'] = f'Are you sure you want to remove student "{exam_enrolled.student.get_full_name()}" from ' \
                         f'exam list '
        context['cancel_url'] = 'exams-list'
        return context


# def otp(request):
#     if request.method == 'POST':
#         form = OTPForm(request.POST)
#         if form.is_valid():

#             otp_code = form.cleaned_data['otp_code']
#             user_id = request.POST.get("user_id", "0")
            
       
#             saved_otp_code = OTP.objects.filter(user_id=user_id,otp_code=otp_code).count()

#             if saved_otp_code > 0:
#                 user = Parent.objects.get(pk=user_id)
#                 login(request, user)

#                 messages.success(request, f'Log In Successful')
#                 return redirect('home')
            
#             messages.success(request, f'Invalid Code')
#             return redirect('login')
#     else:
#         user_id = request.user.id
#         # get the phone number of the logged in user
#         phone_number = User.objects.filter(username=request.user.username).first().phone_number
#         otp_code = get_code()

#         # check if there is any OTP codes related to the currently logged in user in the OTP table
#         otp_data = OTP.objects.filter(user=request.user)

#         # if they are more than 0
#         if otp_data.count() > 0:
#             # delete all the related OTP codes
#             otp_data.delete()
        
#         # save the genertaed OTP code and related user in the OTP Table
#         OTP.objects.create(user=request.user,otp_code=otp_code)

#         # send the OTP code to the user's mobile phone
#         send(phone_number=phone_number,message=f"Log In Code: {otp_code}")

#         # generate the OTP form to be filled in by the user
#         form = OTPForm()

#         # log the user out (in the background), so that you can log them in once they enter correct OTP Password
#         logout(request)

#         # pass the OTP form and the user id into the HTML template as you won't access once you logout a user
#         context = {'form': form, 'user_id': user_id}

#     return render(request, 'users/otp.html', context)