from django.contrib import admin
from .models import Course, CategoryCourse, Lesson, Schedule

admin.site.register(CategoryCourse)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Schedule)