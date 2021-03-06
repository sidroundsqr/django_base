"""Abstract base class for the models which requires Slug field"""

from django.db import models

from utils.helper import get_unique_slug
from utils.models.title_base_model import TitleBaseModel


class SlugBaseModel(TitleBaseModel):
    """Django Abstract base class has slug fields."""
    slug = models.SlugField(unique=True, blank=True, max_length=300)

    class Meta:
        """Setting class a abstract class"""
        abstract = True

    def save(self, *args, **kwargs):
        slug= self.title
        self.slug = get_unique_slug(self, slug, 'slug')
        super().save(*args, **kwargs)
