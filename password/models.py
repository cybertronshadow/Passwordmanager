from django.db import models
from django.db.models.fields import CharField
import uuid


class StoredPassword(models.Model):
    website = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.website
