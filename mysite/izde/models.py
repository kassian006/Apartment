from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


ROLE_CHOICES = (
    ('agent', 'agent'),
    ('client', 'client'),
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
    image = models.ImageField(upload_to='agent_image/', null=True, blank=True)
    areas = models.CharField(max_length=50, null=True, blank=True)
    # email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)],
                                           null=True, blank=True)


# class AgentProfile(UserProfile):
#     position = models.CharField(max_length=80)
#     languages = models.CharField(max_length=122, null=True, blank=True)
#     # active_listings =
#     experience_since = models.DateField()
#     image_company = models.ImageField(upload_to='company_image/', null=True, blank=True)
#     #superagent =
#
#
# class ClientProfile(UserProfile):
#     position = models.CharField(max_length=80)
# #     number of properties


class Category(models.Model):
    category_name = models.CharField(max_length=80)


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_home')
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
    house_roules = models.CharField(max_length=255)
    location = models.CharField(max_length=150)


class HouseImage(models.Model):
    house_image = models.ImageField(upload_to='house_images/')
    hom_image = models.ForeignKey(House, on_delete=models.CASCADE, related_name='image_house')


# class HouseReview(models.Model):
#     client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
#     house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_review')
#     text = models.TextField()
#     stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)],
#                                               null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.client} - {self.house}'
#
#
# class AgentRating(models.Model):
#     client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='clients')
#     agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='agents')
#     rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.agent} - {self.rating}'
#
#
# class AboutUs(models.Model):
#     img = models.ImageField(upload_to='owner_img')
#     about_owner = models.TextField()
#
#     def __str__(self):
#         return f'{self.about_owner}'

