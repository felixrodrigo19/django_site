from datetime import datetime

from django.db import models


class People(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(datetime.now(), blank=True)
