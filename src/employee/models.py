from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(max_length=255, blank=255)

class Employee(models.Model):
    order = models.IntegerField(default=0)
    fullname = models.CharField(_("full name"), max_length=255, blank=255)
    positions = models.ManyToManyField(Position)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

