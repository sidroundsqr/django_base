from django.db import models

from utils.helper import get_unique_slug


class SlugBaseModel(models.Model):
    slug = models.SlugField(unique=True, blank=True, max_length=300)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        slug= self.title
        self.slug = get_unique_slug(self, slug, 'slug')
        super().save(*args, **kwargs)