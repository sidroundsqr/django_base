from django.db import models


class DescriptionBaseModel(models.Model):
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True