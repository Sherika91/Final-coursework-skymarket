import django_filters

from ads.models import Ad
from django_filters.rest_framework import FilterSet


class AdFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ('title',)
