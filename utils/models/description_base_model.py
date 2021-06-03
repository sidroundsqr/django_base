"""Abstract base class for the models which requires Description field"""

from django.db import models


class DescriptionBaseModel(models.Model):
    """Django Abstract base class has description fields."""
    description = models.TextField(blank=True, null=True)

    class Meta:
        """Setting class a abstract class"""
        abstract = True
