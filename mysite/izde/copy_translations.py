# copy_translations.py
import os
import django
from izde.models import (
    UserProfile, AgentProfile, Social, Skill, Hobby, Area, Languages,
    SelectedWork, Experience, Education, House, Location, HouseImage,
    HouseReview, AgentRating, Resume
)

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Словарь моделей и их переводимых полей
MODELS_FIELDS = {
    AgentProfile: ['position'],
    Social: ['platform'],
    Skill: ['skill_name'],
    Hobby: ['hobby_name'],
    Area: ['area_name'],
    Languages: ['language_name'],
    SelectedWork: ['title', 'description'],
    Experience: ['job_title', 'description'],
    Education: ['degree', 'institution_name'],
    House: ['house_name', 'descriptions', 'house_roules'],
    Location: ['location_name'],
    HouseReview: ['text'],
    AgentRating: ['text'],
}

LANGUAGES = ['en', 'ky']  # Целевые языки (английский и кыргызский)
SOURCE_LANG = 'ru'  # Исходный язык — русский

def copy_translations():
    for model, fields in MODELS_FIELDS.items():
        print(f"Копирование данных для модели: {model.__name__}")
        for instance in model.objects.all():
            for field in fields:
                # Получаем исходное значение (например, house_name, которое на русском)
                src_value = getattr(instance, field, None)
                if src_value:
                    # Копируем его в поля других языков
                    for lang in LANGUAGES:
                        field_name = f"{field}_{lang}"
                        if not getattr(instance, field_name, None):  # Копируем только если поле пустое
                            setattr(instance, field_name, src_value)
            instance.save()
        print(f"Завершено копирование для {model.__name__}")

if __name__ == "__main__":
    copy_translations()
    print("Копирование всех данных завершено!")