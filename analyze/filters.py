# -*- coding: utf-8 -*-
# author: itimor

from analyze.models import DomainStatus
from django_filters import rest_framework as filters
from django_filters import TimeRangeFilter


class DomainStatusFilter(filters.FilterSet):
    create_time = TimeRangeFilter()

    class Meta:
        model = DomainStatus
        fields = ['node__name', 'domain', 'create_time']
