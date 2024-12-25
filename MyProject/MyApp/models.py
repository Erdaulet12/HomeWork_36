from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    reset_token = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
