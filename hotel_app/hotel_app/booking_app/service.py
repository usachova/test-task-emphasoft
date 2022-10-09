from django_filters.rest_framework import FilterSet, RangeFilter
from .models import Room


class RoomFilter(FilterSet):
    cost = RangeFilter()
    beds_count = RangeFilter()

    class Meta:
        model = Room
        fields = ['cost', 'beds_count']
