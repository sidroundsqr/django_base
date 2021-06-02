from django.db import models


class TitleBaseModel(models.Model):
    title = models.CharField(max_length=250, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title