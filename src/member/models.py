from django.db import models
from django.utils.translation import gettext_lazy as _


class Member(models.Model):
    order = models.IntegerField(default=0)
    fullname = models.CharField(_("full name"), max_length=255, blank=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_attend = models.BooleanField(default=False)
