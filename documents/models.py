from django.db import models


class Document(models.Model):
    document = models.FileField()
    public = models.BooleanField(default=False)
