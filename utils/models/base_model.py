"""Abstract base class for all the models"""

from django.db import models


class BaseModel(models.Model):
    """Django Abstract base class has created and updated fields."""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Setting class a abstract class"""
        abstract = True
