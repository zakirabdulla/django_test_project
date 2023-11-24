from rest_framework import serializers
from .models import IntervieweeModel, InterviewerModel, InterviewModel


class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerModel
        fields = '__all__'


class IntervieweeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervieweeModel
        fields = '__all__'

# Task 2
# TODO: Create a serializer for InterviewModel

class InterviewSerializer(serializers.ModelSerializer):
    interviewer = InterviewerSerializer()
    interviewee = IntervieweeSerializer()

    class Meta:
        model = InterviewModel
        fields = '__all__'

class InterviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewModel
        fields = '__all__'
