"""Abstract base class for the models which requires Status field"""

from django.db import models

ACTIVE = True
INACTIVE = False


class StatusBaseModel(models.Model):
    """Django Abstract base class has status fields."""

    status = models.BooleanField(default=ACTIVE)

    class Meta:
        """Setting class a abstract class"""
        abstract = True
