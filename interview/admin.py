from django.contrib import admin
from .models import InterviewerModel, IntervieweeModel, InterviewModel


@admin.register(InterviewerModel)
class InterviewerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile')

@admin.register(IntervieweeModel)
class IntervieweeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'skills')

@admin.register(InterviewModel)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('interviewer', 'interviewee', 'start_time', 'end_time', 'feedback', 'status')

# Task 3
# TODO: Register InterviewModel which you created in models.py
