from django.db import models

class BaseDefinitionManager(models.Manager):
    def get_from_name(self, name):
        return query.filter(name__icontains=name)