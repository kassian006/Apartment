from django.contrib import admin
from .models import *


admin.site.register(House)
admin.site.register(Category)
from django.contrib.auth.admin import UserAdmin


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


class DetailAdmin(admin.ModelAdmin):
    inlines = [SocialInline, HobbyInline, SkillInline, AreaInline, LanguagesInline, ExperienceInline, SelectedWorkInline, EducationInline]


admin.site.register(UserProfile)
admin.site.register(AgentProfile, DetailAdmin)
admin.site.register(Resume)
admin.site.register(HouseReview)
admin.site.register(AgentRating)
