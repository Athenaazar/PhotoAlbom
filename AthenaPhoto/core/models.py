from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from django.utils import timezone

from core.tools import upload_image_path


class User(AbstractUser):

    def __str__(self):
        return self.username


class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    code = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Picture(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="pictures")
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_image_path, default='pictures/default.png', blank=True, null=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    size = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def image_size(self):
        if self.size < 1024:
            return f"{self.size} bytes"
        elif self.size < (1024 * 1024):
            return f"{self.size // 1024} kb"
        else:
            return f"{self.size // (1024 * 1024)} mb"

    def title_length(self):
        return len(self.title)
