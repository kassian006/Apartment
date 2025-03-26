from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'user_role',)
        extra_kwargs = {'passwords':{'write only':True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username':instance.username,
                'email':instance.email,
            },
            'access':str(refresh.access_token),
            'refresh':str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username':instance.username,
                'email':instance.email,
            },
            'access':str(refresh.access_token),
            'refresh':str(refresh),
        }


class AgentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'user_role', 'position', 'active_listings', 'experience_since',
                  'superagent', 'social_agent')
        extra_kwargs = {'passwords':{'write only':True}}

    def create(self, validated_data):
        user = AgentProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username':instance.username,
                'email':instance.email,
            },
            'access':str(refresh.access_token),
            'refresh':str(refresh),
        }


class AgentLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username':instance.username,
                'email':instance.email,
            },
            'access':str(refresh.access_token),
            'refresh':str(refresh),
        }



class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_name']


class HouseListSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ['type_home', 'house_name', 'home_image', 'price', 'location', 'bathroom', 'bedroom', 'square',]


class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class HouseDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ['category', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
                  'aminities', 'bathroom_type', 'parking_type', 'number_room', 'floor', 'series',
                  'descriptions', 'owner', 'house_roules', 'location']

# ----------------------------------rent--------------------------------------------------




class HouseListRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['type_home', 'house_name', 'home_image', 'price', 'location', 'bathroom', 'bedroom', 'square',]


class HouseCreateRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class HouseDetailRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['category', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
                  'aminities', 'bathroom_type', 'parking_type', 'number_room', 'floor', 'series',
                  'descriptions', 'owner', 'house_roules', 'location']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'role', 'phone_number']


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['platform', 'social_url']


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['area_name']


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ['language_name']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['hobby_name']


class SelectedWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedWork
        fields = ['title', 'description', 'url']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['job_title', 'description']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['degree', 'institution_name']


class AgentProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['id', 'first_name', 'last_name', 'image', 'position', 'superagent']


class AgentProfileInfoSerializer(serializers.ModelSerializer):
    experience_since = serializers.DateField(format='%Y')
    languages = LanguagesSerializer(many=True, read_only=True)
    areas = AreaSerializer(many=True, read_only=True)


    class Meta:
        model = AgentProfile
        fields = ['first_name', 'last_name', 'image', 'position', 'superagent', 'phone_number', 'areas',
                  'email', 'languages', 'experience_since', 'image_company', 'active_listings']


class AgentProfileDetailSerializer(serializers.ModelSerializer):
    socials = SocialSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    hobbies = HobbySerializer(many=True, read_only=True)
    areas = AreaSerializer(many=True, read_only=True)
    languages = LanguagesSerializer(many=True, read_only=True)
    selected_works = SelectedWorkSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = AgentProfile
        fields = ['first_name', 'last_name', 'image', 'position', 'phone_number', 'areas', 'email', 'socials',
                  'languages', 'active_listings', 'skills', 'hobbies', 'selected_works', 'experiences', 'educations']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class AgentRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentRating
        fields = '__all__'


class HouseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseReview
        fields = '__all__'


class UserProfileEditSerializer(serializers.ModelSerializer):
    location_profile = LocationSerializer(many=True, read_only=True)
    owner_house = HouseListSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'location_profile', 'owner_house']

