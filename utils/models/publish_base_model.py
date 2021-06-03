"""Abstract base class for the models which requires Publish field"""

from django.db import models

PUBLISH = True
UNPUBLISH = False


class PublishBaseModel(models.Model):
    """Django Abstract base class has publish fields."""
    publish = models.BooleanField(default=PUBLISH)

    class Meta:
        """Setting class a abstract class"""
        abstract = True
