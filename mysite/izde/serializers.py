from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import authenticate
from django_rest_passwordreset.models import ResetPasswordToken


class VerifyResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email пользователя
    reset_code = serializers.IntegerField()  # 4-значный код
    new_password = serializers.CharField(write_only=True)  # Новый пароль

    def validate(self, data):
        email = data.get('email')
        reset_code = data.get('reset_code')

        # Проверяем, существует ли указанный код для email
        try:
            token = ResetPasswordToken.objects.get(user__email=email, key=reset_code)
        except ResetPasswordToken.DoesNotExist:
            raise serializers.ValidationError("Неверный код сброса или email.")

        data['user'] = token.user
        return data

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']

        # Устанавливаем новый пароль
        user.set_password(new_password)
        user.save()



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

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def validate(self, data):
        refresh_token = data.get('refresh')
        try:
            # Проверяем, что токен валиден
            token = RefreshToken(refresh_token)
            return data
        except TokenError:
            raise serializers.ValidationError({'detail': 'Недействительный токен.'})

    def save(self):
        # Добавляем токен в черный список
        refresh_token = self.validated_data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()


class AgentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'user_role', 'position', 'active_listings', 'experience_since',)
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


class UserProfileRealtySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_name']


class HouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['type_home', 'house_name', 'home_image', 'price', 'location', 'bathroom', 'bedroom', 'square',]


class RealtyApplicationListSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer(read_only=True)
    class Meta:
        model = House
        fields = ['id', 'owner', 'subject', 'body', 'created_at', 'status_publish']


class RealtyApplicationDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileRealtySerializer(read_only=True)
    location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ['owner', 'property_type', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
                  'aminities', 'bathroom_type', 'parking_type', 'number_room', 'floor', 'series',
                  'descriptions', 'house_roules', 'location', 'status_publish']


class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['property_type', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
                  'aminities', 'bathroom_type', 'parking_type', 'number_room', 'floor', 'series',
                  'descriptions', 'house_roules', 'location']  # Убираем 'owner', чтобы клиент не передавал его

    def create(self, validated_data):
        request = self.context['request']  # Получаем текущего пользователя
        house = House.objects.create(owner=request.user, **validated_data)  # Автоматически назначаем владельца
        return house


class HouseDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ['property_type', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
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
        fields = ['property_type', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
                  'aminities', 'bathroom_type', 'parking_type', 'number_room', 'floor', 'series',
                  'descriptions', 'house_roules', 'location']  # Убираем 'owner', чтобы клиент не передавал его

    def create(self, validated_data):
        request = self.context['request']  # Получаем текущего пользователя
        house = House.objects.create(owner=request.user, **validated_data)  # Автоматически назначаем владельца
        return house


class HouseDetailRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['property_type', 'type_home', 'house_name', 'price', 'bedroom', 'bathroom', 'square',
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


class AgentProfileResumeSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = AgentProfile
        fields = ['first_name', 'last_name', 'image', 'position', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class ResumeListSerializer(serializers.ModelSerializer):
    agent = AgentProfileResumeSerializer(read_only=True)
    class Meta:
        model = Resume
        fields = ['agent', 'status', 'created_date']


class ResumeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['resume']


class AgentProfileRatingSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['email', 'phone_number']


class AgentRatingSerializer(serializers.ModelSerializer):
    agent = AgentProfileResumeSerializer(read_only=True)
    areas = AreaSerializer(many=True, read_only=True)
    agents = AgentProfileRatingSocialSerializer(read_only=True)

    class Meta:
        model = AgentRating
        fields = ['agent', 'areas', 'agents', 'created_date']


class AgentRatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentRating
        fields = ['client', 'agent', 'rating', 'text', 'created_date']


class HouseListRatingSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = House
        fields = ['type_home', 'house_name', 'home_image', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class HouseReviewSerializer(serializers.ModelSerializer):
    house = HouseListRatingSerializer(read_only=True)
    class Meta:
        model = HouseReview
        fields = ['house', 'text']


class HouseReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseReview
        fields = ['client', 'house', 'stars', 'text', 'created_date']



class UserProfileEditSerializer(serializers.ModelSerializer):
    location_profile = LocationSerializer(many=True, read_only=True)
    owner_house = HouseListSerializer(many=True, read_only=True)
    property_count = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['image', 'first_name', 'last_name', 'user_role', 'property_count', 'location_profile', 'phone_number', 'email', 'owner_house']

    def get_property_count(self, obj):
            return obj.get_property_count()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'subject', 'body', 'created_at', 'status', 'is_read']

