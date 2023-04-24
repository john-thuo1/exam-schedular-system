# Exams urls
from django.urls import path, include
from exams.views import (home, about, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView,
                         UnitListView, UnitCreateView, UnitUpdateView, UnitDeleteView,
                         ExamListView, ExamCreateView, ExamUpdateView, ExamDeleteView)

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('course/new/', CourseCreateView.as_view(), name='courses-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
    path('courses', CourseListView.as_view(), name='courses-list'),
    path('unit/new/', UnitCreateView.as_view(), name='units-create'),
    path('unit/<int:pk>/update/', UnitUpdateView.as_view(), name='units-update'),
    path('unit/<int:pk>/delete/', UnitDeleteView.as_view(), name='units-delete'),
    path('units', UnitListView.as_view(), name='units-list'),
    path('exam/new/', ExamCreateView.as_view(), name='exams-create'),
    path('exam/<int:pk>/update/', ExamUpdateView.as_view(), name='exams-update'),
    path('exam/<int:pk>/delete/', ExamDeleteView.as_view(), name='exams-delete'),
    path('exams', ExamListView.as_view(), name='exams-list'),

]
