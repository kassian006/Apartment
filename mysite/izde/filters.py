import django_filters
from django_filters import FilterSet
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


