# from django.contrib import admin
# from .models import *
#
#
# class LocationInline(admin.TabularInline):
#     model = Location
#     extra = 1
#
#
# class LocationAdmin(admin.ModelAdmin):
#     inlines = [LocationInline]
#
# admin.site.register(House, LocationAdmin)
# from django.contrib.auth.admin import UserAdmin
#
#
# class SocialInline(admin.TabularInline):
#     model = Social
#     extra = 1
#
#
# class SkillInline(admin.TabularInline):
#     model = Skill
#     extra = 1
#
#
# class HobbyInline(admin.TabularInline):
#     model = Hobby
#     extra = 1
#
#
# class AreaInline(admin.TabularInline):
#     model = Area
#     extra = 1
#
#
# class LanguagesInline(admin.TabularInline):
#     model = Languages
#     extra = 1
#
#
# class SelectedWorkInline(admin.TabularInline):
#     model = SelectedWork
#     extra = 1
#
#
# class ExperienceInline(admin.TabularInline):
#     model = Experience
#     extra = 1
#
#
# class EducationInline(admin.TabularInline):
#     model = Education
#     extra = 1
#
#
# class DetailAdmin(admin.ModelAdmin):
#     inlines = [SocialInline, HobbyInline, SkillInline, AreaInline, LanguagesInline, ExperienceInline, SelectedWorkInline, EducationInline]
#
#
# admin.site.register(UserProfile)
# admin.site.register(AgentProfile, DetailAdmin)
# admin.site.register(Resume)
# admin.site.register(HouseReview)
# admin.site.register(AgentRating)


# ---------------------------------------------------------------------------------

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    UserProfile, AgentProfile, Social, Skill, Hobby, Area, Languages,
    SelectedWork, Experience, Education, House, Location, HouseImage,
    HouseReview, AgentRating, Resume
)

# Базовый класс для табов перевода
class BaseTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# Inline классы
class LocationInline(admin.TabularInline):
    model = Location
    extra = 1

class SocialInline(admin.TabularInline):
    model = Social
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1

class AreaInline(admin.TabularInline):
    model = Area
    extra = 1

class LanguagesInline(admin.TabularInline):
    model = Languages
    extra = 1

class SelectedWorkInline(admin.TabularInline):
    model = SelectedWork
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

# Классы админки
@admin.register(House)
class LocationAdmin(BaseTranslationAdmin):
    inlines = [LocationInline]
    list_display = ('house_name', 'type_home', 'price', 'owner')

@admin.register(AgentProfile)
class DetailAdmin(BaseTranslationAdmin):
    inlines = [SocialInline, HobbyInline, SkillInline, AreaInline, LanguagesInline,
               ExperienceInline, SelectedWorkInline, EducationInline]
    list_display = ('username', 'position', 'user_role')

@admin.register(UserProfile)
class UserProfileAdmin(BaseTranslationAdmin):
    list_display = ('username', 'user_role', 'email')

@admin.register(Resume)
class ResumeAdmin(BaseTranslationAdmin):
    list_display = ('agent', 'status', 'created_date')

@admin.register(HouseReview)
class HouseReviewAdmin(BaseTranslationAdmin):
    list_display = ('client', 'house', 'stars', 'created_date')

@admin.register(AgentRating)
class AgentRatingAdmin(BaseTranslationAdmin):
    list_display = ('client', 'agent', 'rating', 'created_date')