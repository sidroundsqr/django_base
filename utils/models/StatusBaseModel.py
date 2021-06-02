from django.db import models
ACTIVE = True
INACTIVE = False


class StatusBaseModel(models.Model):
    status = models.BooleanField(default=ACTIVE)

    class Meta:
        abstract = True