from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views


from exams.models import Course, Unit, Exam

# Class Based Views Inherit from the View class or one of its subclasses, 
# and implement methods such as get() and post() to handle HTTP requests

# Create your views here.
@login_required
def home(request): 
    return render(request, 'exams/index.html')


def about(request):
    return render(request, 'exams/about.html')

#-----------------------------------------------------------------------------------------------------------------
# Course Views
class CourseCreateView(CreateView):
    model = Course
    # Fields to include in the form in order to create a new course
    fields = ['name', 'description']
    template_name = 'exams/courses_detail.html'

    # method is called after a successful form submission and, 
    # is used to redirect the user to a success URL, in this case- 'courses-list.
    
    def get_success_url(self):
        return reverse('courses-list')
    
    # Adds a table title to the context by calling the Parent's class get.context_data and extending it
    # Parent Class in this case is CreateView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Course'
        return context


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'description']
    template_name = 'exams/courses_detail.html'

    def get_success_url(self):
        
        return reverse('courses-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Course'
        return context


class CourseListView(ListView):
    model = Course
    template_name = 'exams/courses_list.html'
    context_object_name = 'courses'
    paginate_by = 3


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'exams/confirm_delete.html'

    def get_success_url(self):      
        return reverse('courses-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Course'
        # Retrieves the name of the course we want to delete 
        course_name = Course.objects.get(pk=self.kwargs.get('pk')).name
        context['message'] = f'Are you sure you want to delete the course "{course_name}"'
        # Display a cancel button on confirmation page and if pressed, return use to the courses list
        context['cancel_url'] = 'courses-list'
        return context


# -------------------------------------------------------------------------------------------------------------------------
# Unit Views

class UnitCreateView(CreateView):
    model = Unit
    fields = ['name', 'description', 'course']
    template_name = 'exams/units_detail.html'

    def get_success_url(self):
        return reverse('units-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New unit'
        return context


class UnitUpdateView(UpdateView):
    model = Unit
    fields = ['name', 'description', 'course']
    template_name = 'exams/units_detail.html'

    def get_success_url(self):
        return reverse('units-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update unit'
        return context


class UnitListView(ListView):
    model = Unit
    template_name = 'exams/units_list.html'
    context_object_name = 'units'
    paginate_by = 3


class UnitDeleteView(DeleteView):
    model = Unit
    template_name = 'exams/confirm_delete.html'
    
    def get_success_url(self):
        return reverse('units-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Unit'
        unit_name = Unit.objects.get(pk=self.kwargs.get('pk')).name
        context['message'] = f'Are you sure you want to delete "{unit_name}" unit?'
        context['cancel_url'] = 'units-list'
        return context


# ----------------------------------------------------------------------------------------------------------------------------
# Exam Views

class ExamCreateView(CreateView):
    model = Exam
    fields = ['unit', 'start_time', 'duration','start_date', 'end_date']
    template_name = 'exams/exams_detail.html'

    def get_success_url(self):
        return reverse('exams-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Exam'
        return context


class ExamUpdateView(UpdateView):
    model = Exam
    fields = ['unit', 'start_time','duration','start_date']
    template_name = 'exams/exams_detail.html'

    def get_success_url(self):
        return reverse('exams-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Exam'
        return context


class ExamListView(ListView):
    model = Exam
    template_name = 'exams/exams_list.html'
    context_object_name = 'exams'
    paginate_by = 6


class ExamDeleteView(DeleteView):
    model = Exam
    success_url = '/'
    template_name = 'exams/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Exam'
        exam_name = Exam.objects.get(pk=self.kwargs.get('pk'))
        context['message'] = f'Are you sure you want to delete the following exam "{exam_name}"?'
        context['cancel_url'] = 'exams-list'
        return context
