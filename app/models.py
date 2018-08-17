# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .managers import BaseDefinitionManager

class BaseDefinitionModel(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=100)

    objects = BaseDefinitionManager()
    
    class Meta:
        abstract = True

    def __repr__(self):
        return self.name

class Apps(BaseDefinitionModel):
    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
        ordering = ['code']

   