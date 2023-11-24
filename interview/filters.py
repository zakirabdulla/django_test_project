import django_filters

from .models import InterviewModel


class InterviewFilter(django_filters.FilterSet):
    start_time = django_filters.DateFilter(field_name='start_time', lookup_expr='gte')
    end_time = django_filters.DateFilter(field_name='end_time', lookup_expr='lte')
    class Meta:
        model = InterviewModel
        fields = [ 'status']
