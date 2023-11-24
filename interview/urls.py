from django.urls import path
from .views import (
    interviewee_detail_view, 
    interviewee_view,
    IntervieweeListAPIView,
    IntervieweeDetailAPIView,
    InterviewListCreateAPIView,
    InterviewDetailAPIView,
    InterviewerInterviewsAPIView
 )

urlpatterns = [
    path('interviewee/', IntervieweeListAPIView.as_view(), name='interviewee-list'),
    path('interviewee/<int:id>/', IntervieweeDetailAPIView.as_view(), name='interviewee-detail'),

    path('interview/', InterviewListCreateAPIView.as_view(), name='interviewer-list'),
    path('interview/<int:id>/', InterviewDetailAPIView.as_view(), name='interview-detail'),

    path('interviewer/<int:id>/interviews/', InterviewerInterviewsAPIView.as_view(), name='interviewer-interviews'),

]

# Task 10
# TODO: Add routes for created views
