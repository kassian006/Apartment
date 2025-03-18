from django.db import models
from django.contrib.auth.models import AbstractUser


ROLE_CHOICES = (
    ('agent', 'agent'),
    ('client', 'client'),
)