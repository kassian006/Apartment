from rest_framework import serializers
from .models import UserProfile, House, Category


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class HouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['type_home', 'house_name', 'home_image', 'price', 'location', 'bathroom', 'bedroom', 'square']


class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class HouseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['category', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
                  'aminities', 'bathroom_type', 'parking_type', 'number_room', 'floor', 'series',
                  'descriptions', 'owner', 'house_roules', 'location']

