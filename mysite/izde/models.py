from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


ROLE_CHOICES = (
    ('agent', 'agent'),
    ('client', 'client'),
    ('owner', 'owner')
)

CHOICES_CONDITIONS = (
    ('balcony', 'balcony'),
    ('microwave', 'microwave'),
    ('WiFi', 'WiFi'),
    ('Covered parking', 'covered parking'),
    ('TV', 'TV'),
    ('Central heating', 'central heating'),
    ('Washing_machine', 'washing machine'),
    ('Air-conditioner', 'air-conditioner'),
    ('Tableware', 'tableware'),
    ('Swimming pool', 'swimming pool'),
    ('Gym', 'gym'),
    ('Workspace', 'workspace'),
    ('Pet friendly', 'pet friendly'),
)


class UserProfile(AbstractUser):
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')
    phone_number = PhoneNumberField(null=True, blank=True)
    image = models.ImageField(upload_to='user_image/',null=True, blank=True)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)],
                                           null=True, blank=True)

    def __str__(self):
        return f'{self.username}-{self.user_role}'

    # def get_property_count(self):
    #     """
    #     Возвращает количество домов, принадлежащих пользователю.
    #     Если пользователь не является владельцем, возвращает 0.
    #     """
    #     if self.user_role != 'owner':
    #         return 0
    #     return self.owner_house.count()

    def get_property_count(self):
        owner_house = self.owner_house.all()
        if owner_house.exists():
            return owner_house.count()
        return 0

class AgentProfile(UserProfile):
    position = models.CharField(max_length=80)
    active_listings = models.IntegerField(default=0)
    experience_since = models.DateField()
    image_company = models.ImageField(upload_to='company_image/', null=True, blank=True)
    superagent = models.BooleanField(default=False)

    def get_avg_rating(self):
        ratings = self.agents.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def __str__(self):
        return f"{self.username} - {self.position}-{self.user_role}"

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agent'



class Social(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='socials')
    platform = models.CharField(max_length=50)
    social_url = models.URLField()

    def __str__(self):
        return self.platform


class Skill(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


class Hobby(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='hobbies')
    hobby_name = models.CharField(max_length=50)

    def __str__(self):
        return self.hobby_name


class Area(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='agent_areas')
    area_name = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name


class Languages(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name


class SelectedWork(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='selected_works')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.job_title


class Education(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"


class House(models.Model):
    CHOICES_BATHROOM = (
        ('Combined', 'combined'),
        ('Separate', 'separate')
    )
    CHOICES_HOME = (
        ('Rent', 'rent'),
        ('Buy', 'buy')
    )
    CHOICES_PARKING = (
        ('Ground', 'ground'),
        ('Underground', 'underground'),
        ('No', 'no'),
    )
    SERIA_CHOICES = (
        ('Elite', 'elite'),
        ('105', '105'),
        ('106', '106'),
        ('104', '104'),
        ('Individual project', 'Individual project'),
    )
    CHOICES_PROPERTY = (
        ('Apartment', 'Apartment'),
        ('Villa', 'Villa'),
        ('Townhouse', 'Townhouse'),
        ('Penthouse', 'Penthouse'),
        ('Whole Building', 'Whole Building')
    )
    PUBLISH_CHOICES = (
        ('pending', 'Pending'),  # Ожидает рассмотрения
        ('accepted', 'Accepted'),  # Принято
        ('declined', 'Declined'),  # Отклонено
    )
    property_type = models.CharField(max_length=32, choices=CHOICES_PROPERTY)
    type_home = models.CharField(max_length=32, choices=CHOICES_HOME)
    house_name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    home_image = models.ImageField(upload_to='home_images/', null=True, blank=True)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    square = models.IntegerField()
    aminities = MultiSelectField(choices=CHOICES_CONDITIONS, max_choices=13)
    bathroom_type = models.CharField(max_length=16, choices=CHOICES_BATHROOM)
    parking_type = models.CharField(max_length=32, choices=CHOICES_PARKING)
    number_room = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                                   null=True, blank=True)
    floor = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 12)],
                                             null=True, blank=True)
    series = models.CharField(max_length=32, choices=SERIA_CHOICES)
    descriptions = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner_house')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_publish = models.CharField(max_length=20, choices=PUBLISH_CHOICES, default='pending')
    house_roules = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.house_name}-{self.type_home}'

    def get_avg_rating(self):
        stars = self.house_review.all()
        if stars.exists():
            return round(sum(i.stars for i in stars) / stars.count(), 1)
        return 0


class Location(models.Model):
    location_name = models.CharField(max_length=32)
    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='location_profile')
    house = models.ForeignKey('House', on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return self.location_name


class HouseImage(models.Model):
    house_image = models.ImageField(upload_to='house_images/')
    hom_image = models.ForeignKey(House, on_delete=models.CASCADE, related_name='image_house')


class HouseReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_review')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_review')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)],
                                              null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.client} - {self.house}'


class AgentRating(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='clients')
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='agents')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.agent} - {self.rating}'


class Resume(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='agent_resume')
    resume = models.FileField(upload_to='resume_agents/')
    status = models.CharField(max_length=20, choices=[
        ('declined', 'Declined'),
        ('accepted', 'Accepted')
    ])
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.agent}-{self.resume}'


class Message(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
        ('declined', 'Declined'),
    )

    sender = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpublished')
    is_read = models.BooleanField(default=False)  # Новое поле: прочитано или нет

    def __str__(self):
        return f"{self.sender} - {self.subject} - {self.status}"


