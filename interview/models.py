from django.db import models


class InterviewerModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name


class IntervieweeModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=10, blank=False, null=False)
    skills = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

# Task 1
# TODO: Create an interview model with interviewer, interviewee, start time, end time, feedback, status

class InterviewModel(models.Model):

    class StatusChoices(models.TextChoices):
        SCHEDULED = 'Scheduled'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'

    interviewer = models.ForeignKey(InterviewerModel, on_delete=models.CASCADE, related_name='interviews')
    interviewee = models.ForeignKey(IntervieweeModel, on_delete=models.CASCADE, related_name='interviews')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    feedback = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.SCHEDULED)

    def __str__(self):
        return f'{self.interviewer.name} - {self.interviewee.name} Interview'