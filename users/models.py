from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class User(AbstractUser):
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)