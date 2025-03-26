from modeltranslation.translator import register, TranslationOptions
from .models import (
    UserProfile, AgentProfile, Social, Skill, Hobby, Area, Languages,
    SelectedWork, Experience, Education, House, Location, HouseImage,
    HouseReview, AgentRating, Resume
)

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ()  # Нет текстовых полей для перевода (username и email не переводятся)

@register(AgentProfile)
class AgentProfileTranslationOptions(TranslationOptions):
    fields = ('position',)

@register(Social)
class SocialTranslationOptions(TranslationOptions):
    fields = ('platform',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('skill_name',)

@register(Hobby)
class HobbyTranslationOptions(TranslationOptions):
    fields = ('hobby_name',)

@register(Area)
class AreaTranslationOptions(TranslationOptions):
    fields = ('area_name',)

@register(Languages)
class LanguagesTranslationOptions(TranslationOptions):
    fields = ('language_name',)

@register(SelectedWork)
class SelectedWorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('job_title', 'description')

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('degree', 'institution_name')

@register(House)
class HouseTranslationOptions(TranslationOptions):
    fields = ('house_name', 'descriptions', 'house_roules')

@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('location_name',)

@register(HouseImage)
class HouseImageTranslationOptions(TranslationOptions):
    fields = ()  # Нет текстовых полей для перевода

@register(HouseReview)
class HouseReviewTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(AgentRating)
class AgentRatingTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Resume)
class ResumeTranslationOptions(TranslationOptions):
    fields = ()  # Нет текстовых полей для перевода