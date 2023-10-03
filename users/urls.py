# Users urls 
from django.urls import path, include
from django.contrib.auth import views as auth_views


from users.views import (register,StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
                         ProfessorListView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView,
                        ExamEnrollListView, ExamEnrollCreateView, ExamEnrolledUpdateView, ExamEnrolledDeleteView,
                        ParentListView, ParentCreateView, ParentUpdateView, ParentDeleteView)

urlpatterns = [
   
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('student/new/', StudentCreateView.as_view(), name='students-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='students-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='students-delete'),
    path('students', StudentListView.as_view(), name='students-list'),
    path('professor/new/', ProfessorCreateView.as_view(), name='professors-create'),
    path('professor/<int:pk>/update/', ProfessorUpdateView.as_view(), name='professors-update'),
    path('professor/<int:pk>/delete/', ProfessorDeleteView.as_view(), name='professors-delete'),
    path('professors', ProfessorListView.as_view(), name='professors-list'),
    path('parent/new/', ParentCreateView.as_view(), name='parents-create'),
    path('parent/<int:pk>/update/', ParentUpdateView.as_view(), name='parents-update'),
    path('parent/<int:pk>/delete/', ParentDeleteView.as_view(), name='parents-delete'),
    path('parents', ParentListView.as_view(), name='parents-list'),
    path('exams/create/', ExamEnrollCreateView.as_view(), name='enrolled-students-create'),
    path('exams/<int:pk>/update/', ExamEnrolledUpdateView.as_view(), name='enrolled-students-update'),
    path('exams/<int:pk>/delete/', ExamEnrolledDeleteView.as_view(), name='enrolled-students-delete'),
    path('exams/<int:exam_id>/enrolled/', ExamEnrollListView.as_view(), name='enrolled-students-list'),

]
