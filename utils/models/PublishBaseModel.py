from django.db import models
PUBLISH = True
UNPUBLISH = False


class PublishBaseModel(models.Model):
    publish = models.BooleanField(default=PUBLISH)

    class Meta:
        abstract = True