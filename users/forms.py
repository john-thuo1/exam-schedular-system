from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import systemUser
from users.models import Profile, OTP

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import (Student,Professor,Parent,User)


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        professor = Professor.objects.create(user=user)
        return user


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

class AdminSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        # user.is_staff = True
        user.save()
        student = Parent.objects.create(user=user)
        return user





class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class OTPForm(forms.ModelForm):
    otp_code = forms.CharField(max_length=6)

    class Meta:
        model = OTP
        fields = ['otp_code']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
