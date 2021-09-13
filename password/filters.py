from django.db.models import fields
import django_filters
from .models import *


class PasswordFilter(django_filters.FilterSet):
    class Meta:
        model = StoredPassword
        fields = ['website', 'username']
