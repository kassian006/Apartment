from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


ROLE_CHOICES = (
    ('agent', 'agent'),
    ('client', 'client'),
)


class UserProfile(AbstractUser):
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    image = models.ImageField(upload_to='agent_image/',null=True, blank=True)
    areas = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)],
                                           null=True, blank=True)


class AgentProfile(UserProfile):
    position = models.CharField(max_length=50)
    languages = models.CharField(max_length=122, null=True, blank=True)
    # active_listings =
    experience_since = models.DateField()
    image_company = models.ImageField(upload_to='company_image/', null=True, blank=True)
    #superagent =


class Contact(models.Model):
    contact_info = PhoneNumberField(region='KG')
    user = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f'{self.user}, {self.contact_info}'


class ClientProfile(UserProfile):
    position = models.CharField(max_length=50)
    contact = PhoneNumberField(region='KG')
#     number of properties









