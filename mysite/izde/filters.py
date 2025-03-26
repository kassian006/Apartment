from warnings import filters

import django_filters
from django_filters import FilterSet, CharFilter
from .models import *



class HouseFilter(FilterSet):
    property_type = django_filters.ChoiceFilter(choices=House.CHOICES_PROPERTY)

    class Meta:
        model = House
        fields = {
            'number_room': ['exact'],
            'price': ['gt', 'lt'],
            'property_type': ['exact']
        }


class AgentProfileFilter(FilterSet):
    # Фильтр по полю language_name из связанной модели Languages
    language_name = CharFilter(field_name='languages__language_name', lookup_expr='exact')

    class Meta:
        model = AgentProfile
        fields = ['language_name']


class HouseReviewFilter(FilterSet):
    house_name = CharFilter(field_name='house__house_name', lookup_expr='exact')

    class Meta:
        model = HouseReview
        fields = ['house_name']


class ResumeListFilter(FilterSet):
    username = django_filters.CharFilter(field_name='agents__username', lookup_expr='exact')
    class Meta:
        model = Resume
        fields = ['username']


class AgentRatingFilter(FilterSet):
    username = django_filters.CharFilter(field_name='agent__username', lookup_expr='exact')

    class Meta:
        model = AgentRating
        fields = ['agent']
