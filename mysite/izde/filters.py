import django_filters
from django_filters import FilterSet, CharFilter
from .models import *



class HouseFilter(FilterSet):
    category_property = django_filters.ChoiceFilter(
        field_name="category__property_typ",
        choices=Category.CHOICES_PROPERTY
    )

    class Meta:
        model = House
        fields = {
            'number_room': ['exact'],
            'price': ['gt', 'lt'],
        }


class AgentProfileFilter(FilterSet):
    # Фильтр по полю language_name из связанной модели Languages
    language_name = CharFilter(field_name='languages__language_name', lookup_expr='exact')

    class Meta:
        model = AgentProfile
        fields = ['language_name']

