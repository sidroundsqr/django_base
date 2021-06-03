"""Abstract base class for the models which requires Title (unique) field"""

from django.db import models


class TitleBaseModel(models.Model):
    """Django Abstract base class has title (unique) fields."""

    title = models.CharField(max_length=250, unique=True)

    class Meta:
        """Setting class a abstract class"""
        abstract = True

    def __str__(self):
        return str(self.title)
