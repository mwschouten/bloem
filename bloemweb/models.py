from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FlowerGroup(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name