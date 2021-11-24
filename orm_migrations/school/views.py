from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_ = Student.objects.all().prefetch_related('teacher')
    context = {
                'object_list':student_
              }
    ordering = 'group'
    return render(request, template, context)
