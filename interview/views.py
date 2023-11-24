from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import InterviewModel, IntervieweeModel
from .serializers import InterviewModelSerializer, InterviewSerializer, IntervieweeSerializer
from .filters import InterviewFilter



@api_view(['GET'])
def interviewee_view(request):
    interviewees = IntervieweeModel.objects.all()
    # Task 9
    # TODO: sort interviewees by name (first letter of name)

    serializer = IntervieweeSerializer(interviewees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class IntervieweeListAPIView(ListAPIView):
    serializer_class = IntervieweeSerializer
    queryset = IntervieweeModel.objects.order_by('name').all()
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['email', 'mobile']
    search_fields = ['name', 'email', 'mobile', 'skills']


@api_view(['GET'])
def interviewee_detail_view(request, id):
    try:
        interviewee = IntervieweeModel.objects.get(id=id)
        serializer = IntervieweeSerializer(interviewee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except IntervieweeModel.DoesNotExist:
        return Response({"error_message": "Inteviewee with id:{} does not exist!".format(id)}, status=status.HTTP_404_NOT_FOUND)
    
class IntervieweeDetailAPIView(RetrieveAPIView):
    serializer_class = IntervieweeSerializer
    queryset = IntervieweeModel.objects.all()
    lookup_field = 'id'



class InterviewListCreateAPIView(ListCreateAPIView):
    queryset = InterviewModel.objects.all()
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['interviewer__name', 'interviewee__name', 'feedback']
    filterset_class = InterviewFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InterviewSerializer
        elif self.request.method == 'POST':
            return InterviewModelSerializer
        

class InterviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InterviewModelSerializer
    queryset = InterviewModel.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InterviewSerializer
        else:
            return self.serializer_class
        

class InterviewerInterviewsAPIView(ListAPIView):
    serializer_class = InterviewSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = [ 'interviewee__name', 'feedback']
    filterset_class = InterviewFilter
    
    def get_queryset(self):
        interviewer_id = self.kwargs['id']
        return InterviewModel.objects.filter(interviewer=interviewer_id)


# Task 4
# TODO: Create a view to create an interview
# Task 5
# TODO: Create a view to fetch all interviews
# Task 6
# # TODO: Create a view to fetch an interview by id
# Task 7
# # TODO: Create a view to fetch all interviews of an interviewer
# Task 8
# # TODO: Create a view to update an interview by id


# EXTRA tasks
# Task 11: Add Pagination to all list endpoints
# Task 12: Add filtering to all list endpoints
